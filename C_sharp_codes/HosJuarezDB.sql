-- Create a new table called 'Pacientes'
-- Drop the table if it already exists

-- Create the table in the specified schema
CREATE TABLE Pacientes
(
    Id INT NOT NULL PRIMARY KEY, -- primary key column
    Nombre [NVARCHAR](50) NOT NULL,
    Curp [NVARCHAR](50) NOT NULL,
    Direccion [NVARCHAR](50) NOT NULL,
    Edad INT NOT NULL,
    Habitacion INT NOT NULL
    -- specify more columns here
);