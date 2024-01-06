DO $$ 
DECLARE
    loop_counter INT := 1;
BEGIN
    LOOP
        -- Вставка даних у таблицю Category
        INSERT INTO Category (category_name) 
        VALUES ('InitialCategory' || loop_counter);

        loop_counter := loop_counter + 1;

        -- Умова виходу з циклу
        EXIT WHEN loop_counter > 5;
    END LOOP;
END $$;

