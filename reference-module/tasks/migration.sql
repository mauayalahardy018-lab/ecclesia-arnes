CREATE TABLE tasks (
  id bigserial PRIMARY KEY,
  title text NOT NULL CHECK (length(trim(title)) >= 3)
);
