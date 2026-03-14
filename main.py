# Imports for all the libraries needed to run the whole project

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
from src.config import WINDOW_SIZE, POKEMON_DIR, FALLBACK_IMAGE, STATS, BUTTON_FONT, BUTTON_HEIGHT, BACKGROUND_IMAGE, BUTTON_WIDTH
import winsound
import threading
import wave
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def total_stats(index):
    return sum(get_stats(index))



df = pd.read_csv("pokedex.csv")
pokemon_names = df["name"].tolist()
pokemon_types = df["type1"].tolist()
pokemon_images = sorted(os.listdir(POKEMON_DIR))
selected_index_1 = None
selected_index_2 = None





# opening tk window and disabling the maximising view 
root = Tk()
root.title("Pokedex by Huz")
root.geometry(WINDOW_SIZE)
root.resizable(False, False)

# Listen to the pokemon instrumental theme song in the background while looking through the pokedex
def play_music_loop(filename):
    def loop():
        while True:
            winsound.PlaySound(filename, winsound.SND_FILENAME)
    t = threading.Thread(target=loop, daemon=True)
    t.start()

play_music_loop("sounds/pokemon_theme_song.wav")

# Hear the puch sound when buttons are pressed
def play_sound(path):
    try:
        winsound.PlaySound(path, winsound.SND_FILENAME | winsound.SND_ASYNC)
    except Exception as e:
        print("Sound error:", e)




# Setting image size and getting the file 
bg_image = ImageTk.PhotoImage(Image.open(BACKGROUND_IMAGE))
canvas = Canvas(root, width=1280, height=720)
canvas.create_image(0, 0, anchor=NW, image=bg_image)
canvas.pack(fill="both", expand=True)

def load_pokemon_image(index, size=(200, 200)):
    try:
        img_path = os.path.join(POKEMON_DIR, pokemon_images[index])
    except IndexError:
        img_path = os.path.join(POKEMON_DIR, FALLBACK_IMAGE)
    img = Image.open(img_path).resize(size)
    return ImageTk.PhotoImage(img)

def get_stats(index):
    return [df.loc[index, stat] for stat in STATS]






# listbox 1
scroll_1 = Scrollbar(root)
listbox_1 = Listbox(root, yscrollcommand=scroll_1.set)
scroll_1.config(command=listbox_1.yview)
scroll_1.place(x=310, y=170, height=421)
listbox_1.place(x=25, y=170, width=141, height=421)
for name in pokemon_names:
    listbox_1.insert(END, name)

# listbox 2
scroll_2 = Scrollbar(root)
listbox_2 = Listbox(root, yscrollcommand=scroll_2.set)
scroll_2.config(command=listbox_2.yview)
scroll_2.place(x=260, y=170, height=421)
listbox_2.place(x=163, y=170, width=141, height=421)
for name in pokemon_names:
    listbox_2.insert(END, name)




# labels
pokemon_name_label = Label(root, text="Pokemon Name", fg="white", bg="black", font=("Arial", 11))
pokemon_name_label.place(x=451, y=134, width=209, height=36)
pokemon_image_label = Label(root, bg="black")
pokemon_image_label.place(x=460, y=195, width=200, height=200)
second_name_label = Label(root, text="Pokemon Name", fg="white", bg="black", font=("Arial", 11))
second_name_label.place(x=839, y=134, width=209, height=36)
second_image_label = Label(root, bg="black")
second_image_label.place(x=850, y=185, width=200, height=200)





def select_first(event):
    global selected_index_1
    if not listbox_1.curselection():
        return
    selected_index_1 = listbox_1.curselection()[0]

    # Update name
    pokemon_name_label.config(text=pokemon_names[selected_index_1])

    # Update Pokémon image
    img = load_pokemon_image(selected_index_1)
    pokemon_image_label.config(image=img)
    pokemon_image_label.image = img

    # Update type image
    type_img_path = f"{POKEMON_DIR}/poken_types/{df.loc[selected_index_1, 'type1']}.png"
    type_img = ImageTk.PhotoImage(Image.open(type_img_path).resize((50, 50)))
    if hasattr(select_first, "type_label"):
        select_first.type_label.config(image=type_img)
    else:
        select_first.type_label = Label(root, image=type_img, bg="black")
        select_first.type_label.place(x=400, y=250)
    select_first.type_label.image = type_img

    # Update stats card
    stats_text = "\n".join([f"{s.replace('_', ' ').title()}: {df.loc[selected_index_1, s]}" for s in STATS])
    if hasattr(select_first, "stats_label"):
        select_first.stats_label.config(text=stats_text)
    else:
        select_first.stats_label = Label(root, text=stats_text, fg="white", bg="black", font=("Arial", 10), justify=LEFT)
        select_first.stats_label.place(x=390, y=330)

def select_second(event):
    global selected_index_2
    if not listbox_2.curselection():
        return
    selected_index_2 = listbox_2.curselection()[0]

    # Update name
    second_name_label.config(text=pokemon_names[selected_index_2])

    # Update Pokémon image
    img = load_pokemon_image(selected_index_2)
    second_image_label.config(image=img)
    second_image_label.image = img

    # Update type image
    type_img_path = f"{POKEMON_DIR}/poken_types/{df.loc[selected_index_2, 'type1']}.png"
    type_img = ImageTk.PhotoImage(Image.open(type_img_path).resize((50, 50)))
    if hasattr(select_second, "type_label"):
        select_second.type_label.config(image=type_img)
    else:
        select_second.type_label = Label(root, image=type_img, bg="black")
        select_second.type_label.place(x=790, y=250)
    select_second.type_label.image = type_img

    # Update stats card
    stats_text = "\n".join([f"{s.replace('_', ' ').title()}: {df.loc[selected_index_2, s]}" for s in STATS])
    if hasattr(select_second, "stats_label"):
        select_second.stats_label.config(text=stats_text)
    else:
        select_second.stats_label = Label(root, text=stats_text, fg="white", bg="black", font=("Arial", 10), justify=LEFT)
        select_second.stats_label.place(x=790, y=330)

# Bind selection events
listbox_1.bind("<<ListboxSelect>>", select_first)
listbox_2.bind("<<ListboxSelect>>", select_second)






# Comparison chart which shows a generic bar chart of stats compaed of both pokemon selected 
def comparison_chart():
    if selected_index_1 is None or selected_index_2 is None:
        print("Select two Pokemon first.")
        return
    stats1, stats2 = get_stats(selected_index_1), get_stats(selected_index_2)
    x = np.arange(len(STATS))
    width = 0.35
    plt.figure(figsize=(10, 5))
    plt.bar(x - width/2, stats1, width, label=pokemon_names[selected_index_1])
    plt.bar(x + width/2, stats2, width, label=pokemon_names[selected_index_2])
    plt.xticks(x, [s.replace("_", " ").title() for s in STATS])
    plt.ylabel("Stat Value")
    plt.title("Pokemon Stat Comparison")
    plt.legend()
    plt.tight_layout()
    plt.show()




# Another comparison chart but in a radar format 
def radar_chart():
    if selected_index_1 is None or selected_index_2 is None:
        print("Select two Pokemon first.")
        return
    stats1, stats2 = get_stats(selected_index_1), get_stats(selected_index_2)
    labels = [s.replace("_"," ").title() for s in STATS]
    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
    stats1 += stats1[:1]
    stats2 += stats2[:1]
    angles += angles[:1]
    plt.figure(figsize=(6,6))
    ax = plt.subplot(111, polar=True)
    ax.plot(angles, stats1, label=pokemon_names[selected_index_1])
    ax.fill(angles, stats1, alpha=0.25)
    ax.plot(angles, stats2, label=pokemon_names[selected_index_2])
    ax.fill(angles, stats2, alpha=0.25)
    ax.set_thetagrids(np.degrees(angles[:-1]), labels)
    ax.set_title("Radar Stat Comparison")
    ax.legend()
    plt.show()



# Adds all stats up together and shows side by side comparison of selected pokemon 
def total_stat_chart():
    if selected_index_1 is None or selected_index_2 is None:
        print("Select two Pokemon first.")
        return
    names = [pokemon_names[selected_index_1], pokemon_names[selected_index_2]]
    totals = [total_stats(selected_index_1), total_stats(selected_index_2)]
    plt.figure(figsize=(6,4))
    plt.bar(names, totals)
    plt.ylabel("Total Stats")
    plt.title("Total Base Stat Comparison")
    plt.show()



# Shows the top 10 pokemon for all shown categories
def top_10s():
    df["total"] = df[STATS].sum(axis=1)
    top_attack = df.sort_values("attack", ascending=False).head(10)
    top_defense = df.sort_values("defense", ascending=False).head(10)
    top_speed = df.sort_values("speed", ascending=False).head(10)
    top_total = df.sort_values("total", ascending=False).head(10)
    fig, axes = plt.subplots(2,2, figsize=(14,10))
    axes[0,0].barh(top_attack["name"], top_attack["attack"]); axes[0,0].set_title("Top 10 Attack"); axes[0,0].invert_yaxis()
    axes[0,1].barh(top_defense["name"], top_defense["defense"]); axes[0,1].set_title("Top 10 Defense"); axes[0,1].invert_yaxis()
    axes[1,0].barh(top_speed["name"], top_speed["speed"]); axes[1,0].set_title("Top 10 Speed"); axes[1,0].invert_yaxis()
    axes[1,1].barh(top_total["name"], top_total["total"]); axes[1,1].set_title("Top 10 Total"); axes[1,1].invert_yaxis()
    plt.tight_layout()
    plt.show()




# Pie chart which displays all pokemon in their type category measured in percentage 
def type_distribution_chart():
    counts = df["type1"].value_counts()
    plt.figure(figsize=(7,7))
    plt.pie(counts, labels=counts.index, autopct="%1.1f%%")
    plt.title("Pokemon Type Distribution")
    plt.show()


def auto_battler():
    if selected_index_1 is None or selected_index_2 is None:
        print("Select two Pokemon first.")
        return

    # window for auto battler
    battle_window = Toplevel(root)
    battle_window.title("Auto Battler")
    battle_window.geometry("900x600")
    battle_window.resizable(False, False)

    def load_battle_stats(index):
        stats = df.loc[index, STATS].to_dict()
        return {**stats, "max_hp": stats["hp"]}

    p1, p2 = load_battle_stats(selected_index_1), load_battle_stats(selected_index_2)

    # Load images
    img1 = load_pokemon_image(selected_index_1, size=(200, 200))
    img2 = load_pokemon_image(selected_index_2, size=(200, 200))

    img_label1 = Label(battle_window, image=img1)
    img_label1.image = img1
    img_label1.place(x=50, y=50)

    img_label2 = Label(battle_window, image=img2)
    img_label2.image = img2
    img_label2.place(x=650, y=50)

    # Load type images
    type_img1 = ImageTk.PhotoImage(Image.open(f"pokemon/poken_types/{df.loc[selected_index_1, 'type1']}.png").resize((50, 50)))
    type_img2 = ImageTk.PhotoImage(Image.open(f"pokemon/poken_types/{df.loc[selected_index_2, 'type1']}.png").resize((50, 50)))

    # Place type images above each Pokemon image
    type_label1 = Label(battle_window, image=type_img1, bg="white")
    type_label1.image = type_img1  
    type_label1.place(x=125, y=20)  

    type_label2 = Label(battle_window, image=type_img2, bg="white")
    type_label2.image = type_img2
    type_label2.place(x=735, y=20)  


    # Health bars
    canvas1 = Canvas(battle_window, width=200, height=25, bg="red")
    canvas1.place(x=50, y=260)
    hp_bar1 = canvas1.create_rectangle(0, 0, 200, 25, fill="green")

    canvas2 = Canvas(battle_window, width=200, height=25, bg="red")
    canvas2.place(x=650, y=260)
    hp_bar2 = canvas2.create_rectangle(0, 0, 200, 25, fill="green")

    # Stats display
    stats_text1 = Text(battle_window, width=25, height=10)
    stats_text1.place(x=50, y=300)
    stats_text2 = Text(battle_window, width=25, height=10)
    stats_text2.place(x=650, y=300)

    def update_stats():
        stats_text1.config(state="normal")
        stats_text1.delete("1.0", END)
        stats_text1.insert(END,
            f"{pokemon_names[selected_index_1]}\n"
            f"HP: {p1['hp']}\n"
            f"Attack: {p1['attack']}\n"
            f"Defense: {p1['defense']}\n"
            f"Sp. Atk: {p1['sp_attack']}\n"
            f"Sp. Def: {p1['sp_defense']}\n"
            f"Speed: {p1['speed']}\n"
        )
        stats_text1.config(state="disabled")

        stats_text2.config(state="normal")
        stats_text2.delete("1.0", END)
        stats_text2.insert(END,
            f"{pokemon_names[selected_index_2]}\n"
            f"HP: {p2['hp']}\n"
            f"Attack: {p2['attack']}\n"
            f"Defense: {p2['defense']}\n"
            f"Sp. Atk: {p2['sp_attack']}\n"
            f"Sp. Def: {p2['sp_defense']}\n"
            f"Speed: {p2['speed']}\n"
        )
        stats_text2.config(state="disabled")

    update_stats()

    # Battle log
    battle_log = Text(battle_window, width=80, height=13)
    battle_log.place(x=100, y=465)
    battle_log.insert(END, "Battle Start!\n")
    battle_log.config(state="disabled")

    first_attack = [None]

    def choose_first(attacker_index):
        first_attack[0] = attacker_index
        choice_frame.destroy()
        battle_window.after(500, battle_turn)

    choice_frame = Frame(battle_window)
    choice_frame.place(x=350, y=10)
    Label(choice_frame, text="Choose who attacks first:").pack()
    Button(choice_frame, text=pokemon_names[selected_index_1], command=lambda: choose_first(1)).pack(side=LEFT, padx=10)
    Button(choice_frame, text=pokemon_names[selected_index_2], command=lambda: choose_first(2)).pack(side=LEFT, padx=10)

    def battle_turn():
        nonlocal p1, p2
        attacker, defender = (p1, p2) if first_attack[0] == 1 else (p2, p1)
        attacker_name = pokemon_names[selected_index_1] if first_attack[0] == 1 else pokemon_names[selected_index_2]
        defender_name = pokemon_names[selected_index_2] if first_attack[0] == 1 else pokemon_names[selected_index_1]

        damage = max(1, attacker["attack"] - defender["defense"]//2)
        defender["hp"] -= damage
        if defender["hp"] < 0: defender["hp"] = 0

        canvas1.coords(hp_bar1, 0, 0, 200 * p1["hp"]/p1["max_hp"], 25)
        canvas2.coords(hp_bar2, 0, 0, 200 * p2["hp"]/p2["max_hp"], 25)

        update_stats()

        battle_log.config(state="normal")
        battle_log.insert(END, f"{attacker_name} attacks {defender_name} for {damage} damage! ({defender['hp']} HP left)\n")
        battle_log.see(END)
        battle_log.config(state="disabled")

        if defender["hp"] <= 0:
            battle_log.config(state="normal")
            battle_log.insert(END, f"{defender_name} has DIED! Winner: {attacker_name}\n")
            battle_log.config(state="disabled")
            return

        first_attack[0] = 1 if first_attack[0] == 2 else 2
        battle_window.after(800, battle_turn)



def make_card(pokemon_index, filename=None):
    
    if pokemon_index is None:
        print("No Pokémon selected for card.")
        return

    
    name = df.loc[pokemon_index, "name"]
    stats = df.loc[pokemon_index, STATS]
    type_name = df.loc[pokemon_index, "type1"]

    # Pokemon image
    poke_path = os.path.join(POKEMON_DIR, pokemon_images[pokemon_index])
    poke_img = Image.open(poke_path).resize((650, 650)).convert("RGBA")

    # Type image
    type_path = f"{POKEMON_DIR}/poken_types/{type_name}.png"
    type_img = Image.open(type_path).resize((90, 100)).convert("RGBA")

    # Base card
    card = Image.open("pokemon-card.jpg").convert("RGBA")
    card.paste(type_img, (25, 77), mask=type_img)
    card.paste(poke_img, ((card.width - poke_img.width)//2, 55), mask=poke_img)

    
    draw = ImageDraw.Draw(card)
    font_name = ImageFont.truetype("nova.ttf", 60)
    font_stats = ImageFont.truetype("nova.ttf", 30)

    
    strip_width = 720
    bbox = draw.textbbox((0, 0), name, font=font_name)
    text_width = bbox[2] - bbox[0]
    name_location = ((strip_width - text_width)//2, 525)
    draw.text(name_location, name, fill="white", font=font_name, stroke_width=4, stroke_fill='black')

    
    locations = [(180,635),(370,635),(570,635),(180,740),(370,740),(570,740)]
    for stat_name, loc in zip(STATS, locations):
        draw.text(loc, str(stats[stat_name]), fill="white", font=font_stats, stroke_width=2, stroke_fill='black')

    
    os.makedirs("produced_cards", exist_ok=True)
    if filename is None:
        filename = f"{name}_card.png"
    card.save(os.path.join("produced_cards", filename))
    print(f"Card for {name} saved as produced_cards/{filename}")



visualizer_frame = Frame(root, bg="black")
visualizer_frame.place(x=379, y=554, width=500, height=155)  

def open_music_visualizer_in_frame(wav_file):
    wf = wave.open(wav_file, 'rb')
    frames = wf.readframes(wf.getnframes())
    wf.close()
    audio = np.frombuffer(frames, dtype=np.int16)
    audio = audio / np.max(np.abs(audio))

    window = 2000
    step = 400
    index = [0]

    fig = Figure(figsize=(7, 2), dpi=100)  
    ax = fig.add_subplot(111)
    ax.set_ylim(-1, 1)
    ax.set_xlim(0, window)
    line, = ax.plot([], [], lw=1)

    canvas = FigureCanvasTkAgg(fig, master=visualizer_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=BOTH, expand=True)

    def update():
        start = index[0]
        end = start + window
        if end >= len(audio):
            index[0] = 0
            start = 0
            end = window
        y = audio[start:end]
        x = np.arange(len(y))
        line.set_data(x, y)
        canvas.draw()
        index[0] += step
        visualizer_frame.after(30, update)

    update()

open_music_visualizer_in_frame("sounds/pokemon_theme_song.wav")



# Displays all buttons on screen for the user to press and runs all functions 
Button(
    root,
    text="Compare",
    font=2,
    width=13,
    height=1,
    command=lambda: (
        play_sound("sounds/punch_sfx.wav"),
        comparison_chart()
    )
).place(x=461, y=479)

Button(
    root,
    text="Radar",
    font=BUTTON_FONT,
    width=BUTTON_WIDTH,
    height=BUTTON_HEIGHT,
    command=lambda: (
        play_sound("sounds/punch_sfx.wav"),
        radar_chart()
    )
).place(x=1025, y=566)

Button(
    root,
    text="Totals",
    font=BUTTON_FONT,
    width=BUTTON_WIDTH,
    height=BUTTON_HEIGHT,
    command=lambda: (
        play_sound("sounds/punch_sfx.wav"),
        total_stat_chart()
    )
).place(x=1073, y=518)

Button(
    root,
    text="Top 10s",
    font=BUTTON_FONT,
    width=BUTTON_WIDTH,
    height=BUTTON_HEIGHT,
    command=lambda: (
        play_sound("sounds/punch_sfx.wav"),
        top_10s()
    )
).place(x=1124, y=568)

Button(
    root,
    text="Types",
    font=BUTTON_FONT,
    width=BUTTON_WIDTH,
    height=BUTTON_HEIGHT,
    command=lambda: (
        play_sound("sounds/punch_sfx.wav"),
        type_distribution_chart()
    )
).place(x=1074, y=618)

Button(
    root,
    text="Auto - Battler",
    font=3,
    width=13,
    height=1,
    command=lambda: (
        play_sound("sounds/punch_sfx.wav"),
        auto_battler()
    )
).place(x=630, y=480)

Button(
    root,
    text="Make Card 1",
    font=BUTTON_FONT,
    width=11,
    height=BUTTON_HEIGHT,
    command=lambda: (
        play_sound("sounds/punch_sfx.wav"),
        make_card(selected_index_1)
    )
).place(x=535, y=413)


Button(
    root,
    text="Make Card 2",
    font=BUTTON_FONT,
    width=11,
    height=BUTTON_HEIGHT,
    command=lambda: (
        play_sound("sounds/punch_sfx.wav"),
        make_card(selected_index_2)
    )
).place(x=925, y=413)




root.mainloop()
