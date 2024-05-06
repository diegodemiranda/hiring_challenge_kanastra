--  <ID> é usado como um espaço reservado para um valor específico de ID.
--  Este valor de ID seria o identificador único de um registro específico na tabela.
CREATE TABLE charges (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    government_id VARCHAR(20),
    email VARCHAR(100),
    debt_amount NUMERIC(10,2),
    debt_due_date DATE
);

INSERT INTO charges (name, government_id, email, debt_amount, debt_due_date)
VALUES ('Michelle Mitri', '10067798101', 'example@kanastra.com.br', 990.00, '26-05-2025');

UPDATE charges
SET name = 'Novo Nome', debt_amount = 1500.00
WHERE id = <ID>;

SELECT * FROM charges;

SELECT * FROM charges WHERE id = <ID>;

DELETE FROM charges WHERE id = <ID>;

DELETE FROM charges;




