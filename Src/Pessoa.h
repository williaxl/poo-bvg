#ifndef PESSOA_H
#define PESSOA_H

#include <iostream>
#include <string>

class Pessoa {
private:
    std::string nome;
    std::string telefone;

public:
    Pessoa();
    Pessoa(std::string nome, std::string telefone);
    ~Pessoa();
    void imprimirNome();
    void imprimirTelefone();
};

#endif
