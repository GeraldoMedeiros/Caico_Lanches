BEGIN;
--
-- Create model Endereco
--
CREATE TABLE "pedidoCli_endereco" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "rua" varchar(100) NOT NULL, 
    "bairro" varchar(100) NOT NULL, 
    "numero" varchar(8) NOT NULL, 
    "cidade" varchar(100) NOT NULL, 
    "estado" varchar(100) NOT NULL, 
    "cep" varchar(8) NOT NULL);
--
-- Create model Estabelecimento
--
CREATE TABLE "pedidoCli_estabelecimento" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "nomeFrant" varchar(150) NOT NULL, 
    "social" varchar(255) NOT NULL, 
    "cnpj" varchar(11) NOT NULL UNIQUE, 
    "fone" varchar(11) NOT NULL, 
    "login" varchar(255) NOT NULL, 
    "password" varchar(255) NOT NULL, 
    "responsavel" varchar(150) NOT NULL, 
    "endereco_id" integer NOT NULL REFERENCES "pedidoCli_endereco" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Cliente
--
CREATE TABLE "pedidoCli_cliente" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "nome" varchar(150) NOT NULL, 
    "cpf" varchar(11) NOT NULL UNIQUE, 
    "nascimento" datetime NOT NULL, 
    "fone" varchar(11) NOT NULL, 
    "login" varchar(255) NOT NULL, 
    "password" varchar(255) NOT NULL, 
    "endereco_id" integer NOT NULL REFERENCES "pedidoCli_endereco" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE INDEX "pedidoCli_estabelecimento_endereco_id_e7d05b40" ON "pedidoCli_estabelecimento" ("endereco_id");
CREATE INDEX "pedidoCli_cliente_endereco_id_c03f710e" ON "pedidoCli_cliente" ("endereco_id");
COMMIT;