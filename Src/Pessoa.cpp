#include "Pessoa.h"

Pessoa::Pessoa() : nome(""), telefone("") {}
Pessoa::Pessoa(std::string nome, std::string telefone) : nome(nome), telefone(telefone) {}
Pessoa::~Pessoa() { std::cout << "Objeto " << nome << " destruído." << std::endl; }
void Pessoa::imprimirNome() { std::cout << "Nome: " << nome << std::endl; }
void Pessoa::imprimirTelefone() { std::cout << "Telefone: " << telefone << std::endl; }
