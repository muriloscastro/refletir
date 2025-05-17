def refletir_pensamentos():
    """Espaço de reflexão sobre Pensamentos e Interações."""
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
                print("\nReflexão:")
                print("É comum termos nossas próprias maneiras de fazer as coisas em casa, e elas podem parecer as mais lógicas para nós.")
                print("No entanto, cada membro da família tem suas próprias necessidades e perspectivas. Tentar entender o ponto de vista do outro pode levar a soluções mais harmoniosas.")
                print("Lembre-se: 'estar certo' nem sempre é o mais importante, às vezes, ceder um pouco traz mais paz.")

                retornar_cenario = input("Deseja refletir sobre outra situação em casa? (s/n): ").lower()
                if retornar_cenario != 's':
                    break # Volta ao menu principal de cenários

        elif cenario == '2':
            while True:
                print("\nCenário: Diferenças de opiniões")
                topico = input("Sobre qual tópico você tem uma opinião forte que difere da de outras pessoas (financeiro, religião, etc.)? ")
                sua_opiniao = input(f"Compartilhe brevemente sua opinião sobre {topico}: ")
                opiniao_outra = input("Como você percebe a opinião diferente da(s) outra(s) pessoa(s)? ")
                print("\nReflexão:")
                print(f"Opiniões sobre {topico} podem ser profundamente pessoais e influenciadas por diversas experiências e valores.")
                print("Reconhecer que existem múltiplas perspectivas válidas é fundamental para um diálogo respeitoso.")
                print("Tentar entender a origem da opinião do outro, mesmo que você não concorde, pode enriquecer sua própria visão e fortalecer os laços.")

                retornar_cenario = input(f"Deseja refletir sobre outra diferença de opinião sobre {topico}? (s/n): ").lower()
                if retornar_cenario != 's':
                    break # Volta ao menu principal de cenários

        elif cenario == '3':
            while True:
                print("\nCenário: Divergências no trabalho, academia, trânsito")
                local = input("Em qual ambiente ocorreu a divergência (trabalho, academia, trânsito)? ")
                situacao_divergente = input(f"Descreva brevemente a situação de divergência em {local}: ")
                seu_pensamento = input("Qual foi seu pensamento inicial sobre a situação? ")
                print("\nReflexão:")
                print(f"Em ambientes como o {local}, as divergências podem surgir devido a diferentes prioridades, prazos ou até mesmo estresse.")
                print("Lembre-se que todos estão sujeitos a dias ruins e pressões. Tentar abordar a situação com calma e buscando entender o lado do outro pode facilitar a resolução.")
                print("Às vezes, 'estar certo' em uma pequena disputa não compensa o desgaste de um relacionamento ou a criação de um ambiente tenso.")

                retornar_cenario = input(f"Deseja refletir sobre outra divergência em {local}? (s/n): ").lower()
                if retornar_cenario != 's':
                    break # Volta ao menu principal de cenários

        elif cenario == '4':
            print("Encerrando o programa de reflexão.")
            break # Sai do loop principal e encerra o programa

        else:
            print("Cenário inválido. Por favor, escolha um número entre 1 e 4.")

# Executar a função
if __name__ == "__main__":
    refletir_pensamentos()
