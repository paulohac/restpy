"""

"""

from yoyo import step

__depends__ = {}

steps = [
    step("""
        CREATE TABLE prezis (
                id uuid PRIMARY KEY,
                title text, 
                picture text,
                created_at timestamp DEFAULT now(),
                creator_id uuid,
                creator_name text
        );                        
        CREATE INDEX prezis_title_idx ON prezis (title, created_at);        
    """)
]
