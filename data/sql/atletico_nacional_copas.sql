-- Crear la tabla para almacenar los títulos de Atlético Nacional
CREATE TABLE Atletico_Nacional_Copas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    Competencia VARCHAR(50),
    Año INT,
    Rival VARCHAR(50),
    Resultado_Final VARCHAR(50)
);

-- Insertar los datos relacionados con los títulos
INSERT INTO Atletico_Nacional_Copas (Competencia, Año, Rival, Resultado_Final) VALUES
('Copa Libertadores', 1989, 'Olimpia', '1-0 (global)'),
('Copa Libertadores', 2016, 'Independiente del Valle', '2-1 (global)'),
('Copa Interamericana', 1997, 'Saprissa', '3-2 (global)'),
('Copa Merconorte', 1998, 'Deportivo Cali', '4-1 (global)'),
('Copa Merconorte', 2000, 'Millonarios', '2-1 (global)'),
('Copa Merconorte', 2001, 'Emelec', '3-2 (global)'),
('Superliga Colombiana', 2012, 'Junior', '3-1 (global)'),
('Superliga Colombiana', 2016, 'Santa Fe', '5-0 (global)'),
('Liga Colombiana', 1954, 'Millonarios', '2-0'),
('Liga Colombiana', 1973, 'Deportivo Cali', '3-2 (global)'),
('Liga Colombiana', 1976, 'América de Cali', '4-1 (global)'),
('Liga Colombiana', 1981, 'Santa Fe', '3-1 (global)'),
('Liga Colombiana', 1991, 'América de Cali', '1-0'),
('Liga Colombiana', 1994, 'Millonarios', '1-0'),
('Liga Colombiana', 1999, 'América de Cali', '2-0 (global)'),
('Copa Colombia', 2012, 'Deportivo Pasto', '2-0 (global)'),
('Copa Colombia', 2013, 'Millonarios', '1-0'),
('Copa Colombia', 2016, 'Junior', '2-1 (global)'),
('Recopa Sudamericana', 2017, 'Chapecoense', '5-3 (global)');
