def refletir_pensamentos():
    """
    Função principal que implementa um programa interativo de reflexão textual.
    Utiliza um loop 'while True' externo para apresentar um menu de cenários
    (organização doméstica, diferenças de opiniões, divergências em ambientes diversos)
    e uma opção de saída. A navegação do usuário é baseada na entrada numérica.

    Cada cenário possui um loop 'while True' interno que permite ao usuário
    inserir descrições textuais de situações específicas relacionadas ao tema.
    Após a entrada do usuário, são exibidas reflexões textuais predefinidas
    (atualmente embutidas como strings fixas) relevantes ao cenário.

    Ao final de cada reflexão de cenário, o usuário é perguntado se deseja
    refletir sobre outra situação dentro do mesmo cenário. Uma resposta diferente
    de 's' (case-insensitive) interrompe o loop interno, retornando ao menu principal.

    A opção '4' no menu principal encerra o loop externo, finalizando a execução
    do programa com uma mensagem de encerramento. A função trata entradas inválidas
    com uma mensagem de erro.
    """
    while True:
        print("\nBem-vindo(a) ao espaço de reflexão sobre nossos pensamentos e interações.")
        print("Escolha um dos seguintes cenários para explorar:")
        print("1. Organização e regras em casa")
        print("2. Diferenças de opiniões (financeiro, religião, identidade de genero, pessoas atipicas e críticas familiares)")
        print("3. Divergências no trabalho, escola, academia, trânsito")
        print("4. Sair do programa")

        cenario = input("Digite o número do cenário desejado: ")

        if cenario == '1':
            while True:
                print("\nCenário: Organização e regras em casa")
                situacao = input("Descreva uma situação em que você acredita que sua maneira de organizar/seguir regras em casa é a mais correta: ")
                reação_outros = input("Como as outras pessoas geralmente reagem à sua perspectiva? ")
                print("\nReflexão:\nÉ comum termos nossas próprias maneiras de fazer as coisas em casa, e elas podem parecer as mais lógicas para nós.\nNo entanto, cada membro da família tem suas próprias necessidades e perspectivas. Tentar entender o ponto de vista do outro pode levar a soluções mais harmoniosas.\nLembre-se: 'estar certo' nem sempre é o mais importante, às vezes, ceder um pouco traz mais paz.")
                retornar_cenario = input("Deseja refletir sobre outra situação em casa? (s/n): ").lower()
                if retornar_cenario != 's':
                    break
        elif cenario == '2':
            while True:
                print("\nCenário: Diferenças de opiniões")
                topico = input("Sobre qual tópico você tem uma opinião forte que difere da de outras pessoas (financeiro, religião, etc.)? ")
                sua_opiniao = input(f"Compartilhe brevemente sua opinião sobre {topico}: ")
                opiniao_outra = input("Como você percebe a opinião diferente da(s) outra(s) pessoa(s)? ")
                print("\nReflexão:\nOpiniões sobre {topico} podem ser profundamente pessoais e influenciadas por diversas experiências e valores.\nReconhecer que existem múltiplas perspectivas válidas é fundamental para um diálogo respeitoso.\nTentar entender a origem da opinião do outro, mesmo que você não concorde, pode enriquecer sua própria visão e fortalecer os laços.")
                retornar_cenario = input(f"Deseja refletir sobre outra diferença de opinião sobre {topico}? (s/n): ").lower()
                if retornar_cenario != 's':
                    break
        elif cenario == '3':
            while True:
                print("\nCenário: Divergências no trabalho, escola, academia, trânsito")
                local = input("Em qual ambiente ocorreu a divergência (trabalho, academia, trânsito)? ")
                situacao_divergente = input(f"Descreva brevemente a situação de divergência em {local}: ")
                seu_pensamento = input("Qual foi seu pensamento inicial sobre a situação? ")
                print("\nReflexão:\nEm ambientes como o {local}, as divergências podem surgir devido a diferentes prioridades, prazos ou até mesmo estresse.\nLembre-se que todos estão sujeitos a dias ruins e pressões. Tentar abordar a situação com calma e buscando entender o lado do outro pode facilitar a resolução.\nÀs vezes, 'estar certo' em uma pequena disputa não compensa o desgaste de um relacionamento ou a criação de um ambiente tenso.")
                retornar_cenario = input(f"Deseja refletir sobre outra divergência em {local}? (s/n): ").lower()
                if retornar_cenario != 's':
                    break
        elif cenario == '4':
            print("Encerrando o programa de reflexão.")
            break
        else:
            print("Cenário inválido. Por favor, escolha um número entre 1 e 4.")

if __name__ == "__main__":
    refletir_pensamentos()
