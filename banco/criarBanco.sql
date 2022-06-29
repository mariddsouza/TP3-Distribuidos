
-- -----------------------------------------------------
-- Table `Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Usuario` (
  `cpf` VARCHAR(45) NOT NULL,
  `nome` VARCHAR(100) NOT NULL,
  `senha` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`cpf`));

-- -----------------------------------------------------
-- Table `Movel`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Movel` (
  `idMovel` INTEGER PRIMARY KEY  AUTOINCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `tempoUso` VARCHAR(45) NOT NULL,
  `descricao` VARCHAR(500) NOT NULL,
  `Usuario_cpf` VARCHAR(45) NOT NULL,
  CONSTRAINT `fk_Movel_Usuario1`
    FOREIGN KEY (`Usuario_cpf`)
    REFERENCES `Usuario` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `Proposta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Proposta` (
  `usuarioRequisitante` VARCHAR(45) NOT NULL,
  `usuarioAlvo` VARCHAR(45) NOT NULL,
  `moveisPropostos` INT NOT NULL,
  `moveisRequiridos` INT NOT NULL,
  `status` INT NULL,
  `idProposta` INTEGER PRIMARY KEY  AUTOINCREMENT,
  CONSTRAINT `fk_Usuario_has_Usuario_Usuario`
    FOREIGN KEY (`usuarioRequisitante`)
    REFERENCES `Usuario` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Usuario_has_Usuario_Usuario1`
    FOREIGN KEY (`usuarioAlvo`)
    REFERENCES `Usuario` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Usuario_has_Usuario_Movel1`
    FOREIGN KEY (`moveisPropostos`)
    REFERENCES `Movel` (`idMovel`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Usuario_has_Usuario_Movel2`
    FOREIGN KEY (`moveisRequiridos`)
    REFERENCES `Movel` (`idMovel`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);