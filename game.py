import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def prisoner_dilemma():
    st.header("Dilemma del prigioniero")

    st.write("""
        Il dilemma del prigioniero è un esempio classico di teoria dei giochi che illustra come
        le scelte razionali individuali possano portare a un esito subottimale per entrambi i giocatori.
        Entrambi i prigionieri possono scegliere di tacere (D) o tradire (T).
    """)

    payoff_matrix = pd.DataFrame(
        [[(1, 1), (10, 0)],
         [(0, 10), (3, 3)]],
        index=["Tacere (T)", "Tradire (S)"],
        columns=["Tacere (T)", "Tradire (S)"]
    )

    st.write("Matrice dei payoff:")
    st.dataframe(payoff_matrix)

    player1_choice = st.selectbox("Giocatore 1", ("Tacere", "Tradire"), index=0)
    player2_choice = st.selectbox("Giocatore 2", ("Tacere", "Tradire"), index=0)

    player1_index = 0 if player1_choice == "Tacere" else 1
    player2_index = 0 if player2_choice == "Tacere" else 1

    payoff = payoff_matrix.iloc[player1_index, player2_index]
    st.write(f"Payoff: Giocatore 1: ")
    st.write(payoff[0])
    st.write(f"Payoff: Giocatore 2: ")
    st.write(payoff[1])

    # Aggiunta del pulsante "Calcola"
    calculate_button = st.button("Analizza la mossa")
    if calculate_button:
        if payoff[0] < payoff[1]:
            st.write("La mossa del Giocatore 1 è buona perché offre un payoff maggiore rispetto alla controparte.")
        elif payoff[0] > payoff[1]:
            st.write("La mossa del Giocatore 1 non è buona perché offre un payoff inferiore rispetto alla controparte.")
        else:
            st.write("La mossa del Giocatore 1 è neutrale perché offre lo stesso payoff della controparte.")

        if payoff[1] < payoff[0]:
            st.write("La mossa del Giocatore 2 è buona perché offre un payoff maggiore rispetto alla controparte.")
        elif payoff[1] > payoff[0]:
            st.write("La mossa del Giocatore 2 non è buona perché offre un payoff inferiore rispetto alla controparte.")
        else:
            st.write("La mossa del Giocatore 2 è neutrale perché offre lo stesso payoff della controparte.")

        if player1_choice == "Tradire" and player2_choice == "Tradire":
            st.write("Entrambi i giocatori hanno scelto di tradire (T, T).")
            st.write("Spiegazione:")
            st.write("Nel dilemma del prigioniero, entrambi i giocatori cercano di massimizzare il proprio payoff individuale.")
            st.write("Tuttavia, scegliendo entrambi di tradire, entrambi ottengono un payoff più basso rispetto alla scelta di tacere.")
            st.write("Nonostante ciò, nessuno dei giocatori ha un incentivo a cambiare la propria scelta unilateralemente, poiché qualsiasi cambio porterebbe a un payoff ancora più basso.")
            st.write("Di conseguenza, la scelta di tradire per entrambi i giocatori rappresenta l'equilibrio di Nash in questo caso.")
        elif player1_choice == "Tacere" and player2_choice == "Tacere":
            st.write("Entrambi i giocatori hanno scelto di tacere (S, S).")
            st.write("Spiegazione:")
            st.write("Quando entrambi i giocatori scelgono di tacere, entrambi ottengono un payoff più alto rispetto alla scelta di tradire.")
            st.write("Se uno dei giocatori decidesse di tradire mentre l'altro tace, il giocatore che tradisce otterrebbe un payoff ancora più alto.")
            st.write("Tuttavia, nessuno dei giocatori ha un incentivo a cambiare la propria scelta unilateralemente, poiché otterrebbe un payoff più basso.")
            st.write("Quindi, la scelta di tacere per entrambi i giocatori rappresenta anche un possibile equilibrio di Nash.")
        else:
            st.write("La scelta dei giocatori non rappresenta un equilibrio di Nash in questo caso.")
        

        # Calcolo dei payoff dei giocatori
        payoff_values = [payoff[0], payoff[1]]

        # Creazione del DataFrame per l'istogramma
        hist_data = pd.DataFrame({'Giocatori': ["Giocatore 1", "Giocatore 2"], 'Payoff': payoff_values})

        # Aggiunta dell'istogramma
        st.bar_chart(hist_data.set_index('Giocatori'))



def prisoner_dilemma_quantum():
    st.header("Dilemma del prigioniero nella Quantum Game Theory")

    st.write("""
        Il dilemma del prigioniero nella Quantum Game Theory è una variante del dilemma classico in cui
        i giocatori possono sfruttare la sovrapposizione quantistica per ottenere risultati diversi.
        Entrambi i prigionieri possono scegliere di tacere (D) o tradire (T) in modo quantistico.
    """)

    payoff_matrix = pd.DataFrame(
        [[[(1), (1)], [(0), (5)], [(0.5), (3)]],
         [[(5), (0)], [(3), (3)], [(0.5), (3)]],
         [[(3), (0.5)], [(3), (0.5)], [(2.25), (2.25)]]],
        index=["Tacere (D)", "Tradire (T)", "Quantum Move (Q)"],
        columns=["Tacere (D)", "Tradire (T)", "Quantum Move (Q)"]
    )

    st.write("Matrice dei payoff:")
    st.dataframe(payoff_matrix)

    player1_choice = st.selectbox("Giocatore 1", ("Tacere", "Tradire", "Quantum Move"), index=0)
    player2_choice = st.selectbox("Giocatore 2", ("Tacere", "Tradire", "Quantum Move"), index=0)

    player1_index = 0 if player1_choice == "Tacere" else 1 if player1_choice == "Tradire" else 2
    player2_index = 0 if player2_choice == "Tacere" else 1 if player2_choice == "Tradire" else 2

    payoff = payoff_matrix.iloc[player1_index, player2_index]
    st.write(f"Payoff: Giocatore 1: ")
    st.write(payoff[0])
    st.write(f"Payoff: Giocatore 2: ")
    st.write(payoff[1])

    calculate_button = st.button("Analizza la mossa")
    if calculate_button:
        if payoff[0] > payoff[1]:
            st.write("La mossa del Giocatore 1 è buona perché offre un payoff maggiore rispetto alla controparte.")
        elif payoff[0] < payoff[1]:
            st.write("La mossa del Giocatore 1 non è buona perché offre un payoff inferiore rispetto alla controparte.")
        else:
            st.write("La mossa del Giocatore 1 è neutrale perché offre lo stesso payoff della controparte.")

        if payoff[1] > payoff[0]:
            st.write("La mossa del Giocatore 2 è buona perché offre un payoff maggiore rispetto alla controparte.")
        elif payoff[1] < payoff[0]:
            st.write("La mossa del Giocatore 2 non è buona perché offre un payoff inferiore rispetto alla controparte.")
        else:
            st.write("La mossa del Giocatore 2 è neutrale perché offre lo stesso payoff della controparte.")

        if player1_choice == "Quantum Move" and player2_choice == "Quantum Move":
            st.write("Entrambi i giocatori hanno scelto di effettuare una mossa quantistica (Q, Q).")
            st.write("Spiegazione:")
            st.write("Nel caso in cui entrambi i giocatori scelgano di effettuare una mossa quantistica, il risultato dipenderà dalla specifica implementazione della strategia quantistica utilizzata.")
            st.write("La Quantum Game Theory offre molteplici possibilità di strategie quantistiche che possono portare a risultati diversi.")
            st.write("La scelta di una strategia quantistica richiede una conoscenza avanzata della teoria e delle risorse quantistiche disponibili.")
        elif player1_choice == "Tacere" and player2_choice == "Tacere":
            st.write("Entrambi i giocatori hanno scelto di tacere (D, D).")
            st.write("Spiegazione:")
            st.write("Quando entrambi i giocatori scelgono di tacere in modo classico o quantistico, possono ottenere un payoff più alto rispetto alla scelta di tradire.")
            st.write("La strategia quantistica può consentire una migliore cooperazione e una distribuzione più equa dei payoff tra i giocatori.")
            st.write("Tuttavia, l'efficacia delle strategie quantistiche dipende dalla corretta implementazione e dalla capacità di raggiungere un accordo tra i giocatori.")
            #in questo caso usa Hadamard quindi è un nuovo equilibrio di Nash, spiegalo meglio
            st.write("Quindi, la scelta Q-move per entrambi i giocatori rappresenta un nuovo ottimale equilibrio di Nash.")
        else:
            st.write("La scelta dei giocatori non rappresenta necessariamente un equilibrio di Nash nella Quantum Game Theory.")

        # Calcolo dei payoff dei giocatori
        payoff_values = [payoff[0], payoff[1]]

        # Creazione del DataFrame per l'istogramma
        hist_data = pd.DataFrame({'Giocatori': ["Giocatore 1", "Giocatore 2"], 'Payoff': payoff_values})

        # Aggiunta dell'istogramma
        st.bar_chart(hist_data.set_index('Giocatori'))


index = st.sidebar.selectbox("Scegli la teoria", ("Classica", "Quantistica"), index=0)
if index == "Classica":
    prisoner_dilemma()

elif index == "Quantistica":
    prisoner_dilemma_quantum()


