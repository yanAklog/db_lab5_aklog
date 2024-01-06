DO $$ 
DECLARE
    loop_counter INT := 1;
BEGIN
    LOOP
        -- Вставка данных в таблицу Category
        INSERT INTO Category (category_name) 
        VALUES ('InitialCategory' || loop_counter);

        loop_counter := loop_counter + 1;

        -- Условие выхода из цикла
        EXIT WHEN loop_counter > 5;
    END LOOP;
END $$;

