# Computador de 8 Bits no Logisim

Projeto prático desenvolvido no âmbito da disciplina de Organização de Computadores, focado na construção do ciclo completo de funcionamento de um processador de 8 bits do zero, utilizando o simulador Logisim.

---

## Contexto e Referências

Este repositório engloba os trabalhos desenvolvidos na disciplina de Organização de Computadores. O desenvolvimento dos circuitos, do montador e da arquitetura do computador foi baseado nas especificações e conceitos apresentados no livro:
> **SCOTT, J. Clark.** *But How Do It Know? The basic principles of computers for everyone.* John C Scott, 2009.

![Visão Geral do Computador de 8 Bits no Logisim](/img/imagem_circuito.png)

---

## Objetivos do Projeto

- **Projetar e construir os componentes centrais da CPU e memória:**
  - **ULA (Unidade Lógica e Aritmética):** Somador, comparador, *shifter* (deslocador) e seletores.
  - **Registradores:** Armazenamento temporário de dados e estado.
  - **Memória RAM:** Endereçamento e manipulação de leitura/escrita.
  - **Unidade de Controle (UC):** Gerenciamento do ciclo de instrução via *Clocks*, *Steps* e *Stepper*.
  - **Barramentos (Buses):** Trafegabilidade de dados e endereços entre componentes.
  - **Módulos de E/S (I/O):** Entrada e saída de dados.
- **Definir o Conjunto de Instruções (ISA):** Criação das instruções executáveis pela arquitetura.
- **Desenvolver um Montador (Assembler):** Projeto prático desenvolvido na disciplina para traduzir código escrito em linguagem Assembly para código de máquina (binário/hexadecimal) interpretável pelo circuito no Logisim.
- **Executar Programas:** Testar a execução completa de programas montados e carregados na memória RAM.

---

## Conceitos Aplicados e Aprendizados

Ao longo dos trabalhos desenvolvidos na disciplina, foram explorados e consolidados diversos conceitos fundamentais de organização e arquitetura de computadores:

- **Lógica Digital:** Operadores lógicos, álgebra booleana e construção de portas lógicas complexas.
- **Transferência de Dados entre Registradores e RAM:** Leitura e escrita síncrona controladas por barramentos e sinais de enable/clock.
- **Ciclo de Instrução (Fetch, Decode, Execute):**
  - **IAR (Instruction Address Register):** Contador de programa que armazena o endereço da próxima instrução.
  - **IR (Instruction Register):** Registrador de instrução que mantém a instrução atual durante a decodificação.
  - **Bus 1 e Barramento Central:** Rotas internas de controle e movimentação de dados.
- **Temporização e Controle:** Sinais de *Clock*, divisão por *Steps* (*Stepper*) para coordenação do fluxo das instruções.
- **Construção de Ferramentas de Suporte:** Desenvolvimento de um montador próprio para automação da tradução do código Assembly para instruções de máquina.
- **Escalabilidade:** Estudo comparativo entre a arquitetura desenvolvida de 8 bits e sistemas de 16 bits.

---

## Tecnologias Utilizadas

- **Logisim:** Ferramenta de simulação e projeto de circuitos lógicos digitais.
- **Linguagem de Montagem (Assembly) & Montador Próprio:** Desenvolvimento de um montador dedicado para codificação e tradução dos programas de teste.

---

## Como Executar os Projetos no Logisim

1. **Pré-requisitos:**
   - Possuir o Java instalado na máquina.
   - Baixar o executável do Logisim (arquivo `.jar`).

2. **Abrindo o Circuito:**
   - Abra o Logisim.
   - Vá em `File > Open...` e selecione o arquivo principal do projeto (ex: `computador_8bits.circ`).

3. **Carregando um Programa:**
   - Execute o montador desenvolvido no projeto para converter o código em Assembly para o formato de imagem de memória legível pelo Logisim.
   - Clique com o botão direito sobre o componente da Memória RAM no Logisim.
   - Selecione a opção "Load Image..." e escolha o arquivo binário/hexadecimal gerado pelo montador.

4. **Executando:**
   - Ative a simulação no menu `Simulate > Ticks Enabled` (ou avance os passos manualmente pressionando `Ctrl + K` / `Cmd + K`).
   - Observe os dados trafegando pelos barramentos, a atualização dos registradores e a alteração dos estados da memória.