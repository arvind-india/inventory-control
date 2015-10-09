"""
So this is where all the SQL commands live
"""

CREATE_SQL = ("""
CREATE TABLE IF NOT EXISTS component_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type VARCHAR(255) UNIQUE
);
""",
"""
CREATE TABLE IF NOT EXISTS components (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    serial_number VARCHAR(255),
    sku VARCHAR(255),
    type INTEGER,
    status INTEGER,
    FOREIGN KEY (type) REFERENCES component_type(id)
);
""",
"""
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_number INTEGER
);
""",
"""
CREATE TABLE IF NOT EXISTS project_components (
    project_id INTEGER,
    component_id INTEGER,
    FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE,
    FOREIGN KEY (component_id) REFERENCES components(id) ON DELETE CASCADE
);
""")

ADD_COMPONENT_TYPE = """INSERT INTO component_type (type) VALUES ('{text}')
"""

GET_COMPONENT_TYPE="""SELECT * FROM component_type WHERE type='{text}'"""

DELETE_COMPONENT_TYPE = """DELETE FROM component_type WHERE type='{text}'
"""

SELECT_ALL_COMPONENTS = """
SELECT * FROM components INNER JOIN component_type
 ON components.type = component_type.id;
 """

ADD_COMPONENT = """
INSERT INTO components (serial_number, sku, type)
 VALUES ('{serial_number}', '{sku}',
         (SELECT id FROM component_type WHERE type = '{type}'));
"""

ADD_COMPONENT_TO_PROJECT = """
INSERT INTO project_components (project_id, component_id)
  VALUES ((SELECT id FROM projects WHERE product_number = '{project_number}'),
          (SELECT id FROM components WHERE serial_number = '{serial_number}'))
"""

# Project SQL
ADD_PROJECT = "INSERT INTO projects (product_number) VALUES ('{text}')"

DELETE_PROJECT = """
DELETE FROM projects WHERE product_number='{text}'
"""


GET_PROJECT_BY_STATUS = """
SELECT projects.product_number, ct.type FROM projects
  INNER JOIN components co
  INNER JOIN project_components pc ON pc.component_id = co.id
  INNER JOIN component_type ct ON ct.id = co.type
  WHERE pc.project_id = projects.id
"""
#GET_PROJECT_BY_STATUS = "SELECT * FROM project_components;"

DROP_SQL = ("DROP TABLE project_components",
            "DROP TABLE projects",
            "DROP TABLE components",
            "DROP TABLE component_type")
