#include "Pessoa.h"
#include <vector>

int main() {
    std::vector<Pessoa> pessoas;
    pessoas.push_back(Pessoa("João Silva", "99999-1111"));
    pessoas.push_back(Pessoa("Maria Souza", "99988-2222"));
    pessoas.push_back(Pessoa("Pedro Alves", "99977-3333"));

    for (Pessoa& p : pessoas) {
        p.imprimirNome();
        p.imprimirTelefone();
    }

    return 0;
}
