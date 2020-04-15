use treinamento

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- LIMPEZA DOS REGISTROS EXISTENTES
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
BEGIN
	DECLARE @tabelas TABLE(nome_tabela VARCHAR(100))
	INSERT INTO @tabelas (nome_tabela)
	VALUES
		('clinic_patient'),
		('clinic_tutor'),
		('clinic_veterinarian'),
		('clinic_proceduretype'),
		('clinic_coat')		

	DECLARE @ComandoLimparTabelas NVARCHAR(400)
	DECLARE cursor_tabelas CURSOR FAST_FORWARD FOR
		SELECT CONCAT('DELETE FROM ', nome_tabela, 
				' IF EXISTS (SELECT * FROM sys.identity_columns WHERE OBJECT_NAME(OBJECT_ID) = ''', nome_tabela, 
				''' AND LAST_VALUE IS NOT NULL) DBCC CHECKIDENT(', nome_tabela, ', RESEED, 0)')
		FROM @tabelas

	OPEN cursor_tabelas
	FETCH NEXT FROM cursor_tabelas INTO @ComandoLimparTabelas
	WHILE @@FETCH_STATUS = 0
	BEGIN
		EXEC sp_executesql @ComandoLimparTabelas
		FETCH NEXT FROM cursor_tabelas INTO @ComandoLimparTabelas
	END
	CLOSE cursor_tabelas
	DEALLOCATE cursor_tabelas
END




insert into clinic_coat  values
('Branco'),
('Preto'),
('Cinza'),
('Tricolor'),
('Tigrado'),
('Siamês');

insert into clinic_proceduretype values
('Consulta'),
('Exame'),
('Cirurgia');

insert into clinic_veterinarian values
('Veterinario 1',123),
('Veterinario 2',124)


insert into clinic_tutor values
('fulano','123456')

 
  insert into clinic_patient values
('teste',getdate(),null,1,1,1)