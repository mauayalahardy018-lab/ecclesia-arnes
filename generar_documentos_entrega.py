"""Construye las dos versiones Word de la entrega desde sus fuentes Markdown."""
from pathlib import Path
import re

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

WORKSPACE = Path(__file__).resolve().parent.parent
OUTPUTS = [
    (
        WORKSPACE / "ecclesia-arnes" / "ARNES_FINAL.md",
        WORKSPACE / "ecclesia-arnes" / "Arnes_Ecclesia_Final_2026-11-01.docx",
        "ARNÉS DE DESARROLLO",
    ),
    (
        WORKSPACE / "ecclesia-proyecto" / "docs" / "defensa_oral_completa.md",
        WORKSPACE / "ecclesia-proyecto" / "docs" / "Defensa_Oral_Ecclesia_2026-11-01.docx",
        "GUION DE DEFENSA ORAL",
    ),
]


def add_inline(paragraph, text):
    parts = re.split(r"(\*\*[^*]+\*\*|`[^`]+`)", text)
    for part in parts:
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            run = paragraph.add_run(part[2:-2])
            run.bold = True
        elif part.startswith("`") and part.endswith("`"):
            run = paragraph.add_run(part[1:-1])
            run.font.name = "Consolas"
            run.font.size = Pt(8)
        else:
            paragraph.add_run(part)


def cell_shading(cell, fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    tc_pr.append(shd)


def build(source, output, header_label):
    document = Document()
    section = document.sections[0]
    section.page_width = Cm(21.59)
    section.page_height = Cm(27.94)
    section.top_margin = Cm(1.8)
    section.bottom_margin = Cm(1.7)
    section.left_margin = Cm(2.25)
    section.right_margin = Cm(2.0)
    for style_name, size in [("Normal", 9.5), ("Title", 24), ("Heading 1", 15), ("Heading 2", 11.5), ("Heading 3", 10)]:
        style = document.styles[style_name]
        style.font.name = "Aptos" if style_name == "Normal" else "Aptos Display"
        style.font.size = Pt(size)
        style.font.color.rgb = RGBColor(0, 0, 0)
        style.paragraph_format.space_after = Pt(6 if style_name == "Normal" else 5)
        if style_name != "Normal":
            style.font.bold = True
            style.paragraph_format.space_before = Pt(10)
            style.paragraph_format.keep_with_next = True
    title_style_pr = document.styles["Title"]._element.get_or_add_pPr()
    title_border = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "nil")
    title_border.append(bottom)
    title_style_pr.append(title_border)
    document.styles["Normal"].paragraph_format.line_spacing = 1.1
    section.header.paragraphs[0].text = f"ECCLESIA  |  {header_label}  |  01/11/2026"
    section.header.paragraphs[0].style = "Caption"
    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    footer.add_run("Ecclesia  ·  Página ")
    page = OxmlElement("w:fldSimple")
    page.set(qn("w:instr"), "PAGE")
    footer._p.append(page)

    lines = source.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line.startswith("| "):
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                raw = lines[i].strip()
                if not re.fullmatch(r"\|[\s:\-|]+\|", raw):
                    block.append([part.strip() for part in raw.strip("|").split("|")])
                i += 1
            if block:
                columns = max(len(row) for row in block)
                table = document.add_table(rows=1, cols=columns)
                table.alignment = WD_TABLE_ALIGNMENT.CENTER
                table.style = "Table Grid"
                table.autofit = True
                for j, value in enumerate(block[0]):
                    table.rows[0].cells[j].text = value.replace("`", "")
                    cell_shading(table.rows[0].cells[j], "24463B")
                    for run in table.rows[0].cells[j].paragraphs[0].runs:
                        run.bold = True
                        run.font.color.rgb = RGBColor(255, 255, 255)
                        run.font.size = Pt(8)
                tr_pr = table.rows[0]._tr.get_or_add_trPr()
                repeat = OxmlElement("w:tblHeader")
                repeat.set(qn("w:val"), "true")
                tr_pr.append(repeat)
                for row_index, values in enumerate(block[1:]):
                    cells = table.add_row().cells
                    for j in range(columns):
                        cells[j].text = values[j].replace("`", "") if j < len(values) else ""
                        cells[j].vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
                        if row_index % 2:
                            cell_shading(cells[j], "F0F4F0")
                        for p in cells[j].paragraphs:
                            p.paragraph_format.space_after = Pt(2)
                            for run in p.runs:
                                run.font.size = Pt(8)
                document.add_paragraph()
            continue
        if line.startswith("# "):
            title = document.add_paragraph(style="Title")
            add_inline(title, line[2:])
            p_border = OxmlElement("w:pBdr")
            p_bottom = OxmlElement("w:bottom")
            p_bottom.set(qn("w:val"), "nil")
            p_border.append(p_bottom)
            title._p.get_or_add_pPr().append(p_border)
        elif line.startswith("## "):
            document.add_heading(line[3:], level=1)
        elif line.startswith("### "):
            document.add_heading(line[4:], level=2)
        elif re.match(r"^\d+\. ", line):
            p = document.add_paragraph(style="List Number")
            add_inline(p, re.sub(r"^\d+\. ", "", line))
        elif line.startswith("- "):
            p = document.add_paragraph(style="List Bullet")
            add_inline(p, line[2:])
        else:
            p = document.add_paragraph()
            add_inline(p, line)
        i += 1
    document.save(output)
    print(output)


for item in OUTPUTS:
    build(*item)
