# 🧑‍💻 Projeto: Sistema "Cleitinho TI"

## 📬 Mensagem do Cliente

> **Assunto:** URGENTE - Preciso de um sistema pra minha loja! Salvem o Cleitinho!

De: *Cleitinho TI Soluções em Informática* (cleitinho.ti@emailaleatorio.com)  
Para: *Futuros Desenvolvedores de Software*

---

Meu nome é **Cleitinho**, e eu tenho uma pequena loja de manutenção de computadores aqui no bairro.  
O negócio está crescendo, graças a Deus, mas eu estou ficando maluco! Eu controlo tudo num caderninho, e já perdi cliente, esqueci de cobrar serviço e até perdi peça de cliente.  
A situação está caótica.

Falaram que vocês são os melhores e podem construir um programa pra me salvar. Eu não entendo nada de "linguagem de computador", só preciso de um sistema que funcione.

---

## ⚙️ O que o sistema precisa fazer

### 1. Cadastro de Clientes
- Guardar **nome**, **telefone** e **e-mail** de cada cliente.  
- Permitir **listar** todos os clientes.  
- Permitir **buscar** um cliente específico (por nome).

### 2. Gerenciar os Serviços
- Registrar **equipamento** e **descrição do problema** (ex: "não liga", "tela quebrada").  
- Associar cada equipamento a um cliente já cadastrado.  
- Atualizar o **status** do serviço:  
  - Na bancada  
  - Aguardando peça  
  - Pronto para retirada  
  - Entregue  
- Registrar o **valor** do serviço.

### 3. Controle de Peças
- Cadastrar **nome da peça**, **quantidade** e **preço de custo**.  
- Dar **baixa** no estoque quando uma peça for usada num serviço.

### 4. Relatórios Simples
- Listar serviços com status **"Pronto para retirada"**.  
- Listar peças com **estoque baixo** (menos de 5 unidades).

---

## 🧩 Requisitos Importantes

- O programa deve rodar no **console (terminal)**.  
- Deve ter **menus simples** (ex: "Digite 1 para Clientes, 2 para Serviços...").  
- O sistema **não pode travar** se o usuário digitar algo inválido.

---

## 🧱 Lista de Requisitos – Sistema "Cleitinho TI"

### ✅ Requisitos Funcionais

#### 1. Módulo de Clientes
- [ ✅ ] Cadastro de novos clientes: nome, telefone, e-mail  
- [ ✅ ] Listagem de todos os clientes  
- [ ✅ ] Busca de cliente pelo nome  

#### 2. Módulo de Serviços
- [ ✅ ] Registro de novo serviço/equipamento para cliente existente  
- [ ✅ ] Descrição do problema  
- [ ✅ ] Valor do serviço  
- [ ✅ ] Atualização do status ("Na bancada", "Aguardando peça", "Pronto para retirada", "Entregue")  

#### 3. Módulo de Estoque de Peças
- [ ✅ ] Cadastro de peças: nome, quantidade, preço de custo  
- [ ✅ ] Baixa de quantidade ao usar peça  

#### 4. Módulo de Relatórios
- [ ✅ ] Relatório de serviços "Pronto para retirada"  
- [ ✅ ] Relatório de peças com estoque < 5 unidades  

---

### ⚙️ Requisitos Não Funcionais

#### 1. Interface # -=-=-=-=-=-=-=- LUAN -=-=-=-=-=-=-=-=-
- [ ] Operar inteiramente via console  
- [ ] Navegação por menus de texto  

#### 2. Robustez
- [ ] Tratar entradas inválidas (letras em campos numéricos, etc.)  

#### 3. Linguagem e Persistência
- [ ] Feito em **Python com Programação Orientada a Objetos (POO)**  
- [ ] Dados podem ser salvos em **memória**, **arquivo** ou **banco de dados**  

---

## 💡 Observação
> O objetivo é criar um sistema simples, robusto e funcional para atender as demandas reais da loja do Cleitinho.
