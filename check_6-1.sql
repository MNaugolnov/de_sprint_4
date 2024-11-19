DROP TABLE IF EXISTS stage.dq_checks_results;

CREATE TABLE stage.dq_checks_results (
    table_name VARCHAR(255),         -- Название таблицы
    dq_check_name VARCHAR(255),      -- Название проверки
    datetime TIMESTAMP,              -- Дата выполнения проверки
    dq_check_result NUMERIC(8,2)     -- Результат проверки (0 или 1)
);


