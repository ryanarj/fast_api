CREATE TABLE IF NOT EXISTS players (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid (),
  name TEXT,
  number INT,
  position INT,
  team TEXT
);
