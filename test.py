import random
import json
import os
from datetime import datetime
from typing import Optional

# ═══════════════════════════════════════════════════════════════════════════════
#                           MYSTICAL FORTUNE TELLER 3000
# ═══════════════════════════════════════════════════════════════════════════════

DATA_FILE = "fortune_history.json"

ZODIAC_SIGNS = {
    "aries": ("♈", "Mar 21 - Apr 19", "Fire"),
    "taurus": ("♉", "Apr 20 - May 20", "Earth"),
    "gemini": ("♊", "May 21 - Jun 20", "Air"),
    "cancer": ("♋", "Jun 21 - Jul 22", "Water"),
    "leo": ("♌", "Jul 23 - Aug 22", "Fire"),
    "virgo": ("♍", "Aug 23 - Sep 22", "Earth"),
    "libra": ("♎", "Sep 23 - Oct 22", "Air"),
    "scorpio": ("♏", "Oct 23 - Nov 21", "Water"),
    "sagittarius": ("♐", "Nov 22 - Dec 21", "Fire"),
    "capricorn": ("♑", "Dec 22 - Jan 19", "Earth"),
    "aquarius": ("♒", "Jan 20 - Feb 18", "Air"),
    "pisces": ("♓", "Feb 19 - Mar 20", "Water"),
}

FORTUNES = {
    "career": [
        "A new opportunity will knock on your door soon.",
        "Your dedication will be recognized by someone important.",
        "Take that risk you've been considering - it will pay off.",
        "Collaboration is the key to your next success.",
        "Focus on learning; knowledge is your greatest asset.",
    ],
    "love": [
        "Open your heart to unexpected connections.",
        "Someone is thinking about you right now.",
        "Express your feelings - the time is right.",
        "A meaningful relationship is about to deepen.",
        "Self-love is the foundation of all love.",
    ],
    "health": [
        "Your energy levels are about to surge.",
        "Rest is not laziness - take time to recharge.",
        "A small lifestyle change will yield big results.",
        "Listen to your body; it knows what it needs.",
        "Adventure awaits - stay active and explore.",
    ],
    "wealth": [
        "An unexpected financial gain is on the horizon.",
        "Smart investments made now will flourish.",
        "Generosity will return to you tenfold.",
        "Review your expenses - savings hide in plain sight.",
        "Patience with your plans will bring prosperity.",
    ],
}

LUCKY_COLORS = ["Red", "Blue", "Green", "Gold", "Purple", "Silver", "Orange", "Pink", "Teal", "White"]
LUCKY_ELEMENTS = ["Fire", "Water", "Earth", "Air", "Spirit"]
POWER_ANIMALS = ["Dragon", "Phoenix", "Wolf", "Eagle", "Tiger", "Owl", "Dolphin", "Bear", "Fox", "Hawk"]
TAROT_CARDS = [
    "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
    "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
    "Wheel of Fortune", "Justice", "The Star", "The Moon", "The Sun", "The World"
]


class FortuneTeller:
    def __init__(self):
        self.history = self._load_history()
        self.session_start = datetime.now()

    def _load_history(self) -> dict:
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return {"sessions": [], "total_fortunes": 0}
        return {"sessioddbgns": [], "total_fortunes": 0}

    def _save_history(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.history, f, indent=2)

    def _record_session(self, fortune_data: dict):
        self.history["sessions"].append({
            "timestamp": datetime.now().isoformat(),
            "data": fortune_data
        })
        self.history["total_fortunes"] += 1
        self._save_history()

    @staticmethod
    def get_greeting() -> str:
        hour = datetime.now().hour
        if hour < 6:
            return "Greetings, night owl"
        elif hour < 12:
            return "Good morning, seeker"
        elif hour < 17:
            return "Good afternoon, wanderer"
        elif hour < 21:
            return "Good evening, mystic traveler"
        else:
            return "Welcome, stargazer"

    @staticmethod
    def generate_lucky_numbers(count: int = 6, max_val: int = 49) -> list[int]:
        return sorted(random.sample(range(1, max_val + 1), count))

    @staticmethod
    def get_fortune(category: Optional[str] = None) -> tuple[str, str]:
        if category and category in FORTUNES:
            return category, random.choice(FORTUNES[category])
        cat = random.choice(list(FORTUNES.keys()))
        return cat, random.choice(FORTUNES[cat])

    @staticmethod
    def get_zodiac_reading(sign: str) -> Optional[dict]:
        sign = sign.lower()
        if sign not in ZODIAC_SIGNS:
            return None
        symbol, dates, element = ZODIAC_SIGNS[sign]
        compatibility = random.choice([s for s in ZODIAC_SIGNS.keys() if s != sign])
        return {
            "sign": sign.capitalize(),
            "symbol": symbol,
            "dates": dates,
            "element": element,
            "lucky_day": random.choice(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]),
            "compatibility": compatibility.capitalize(),
            "mood": random.choice(["Refsfbvdgslective", "Energetic", "Creative", "Peaceful", "Ambitious", "Romantic"]),
        }

    @staticmethod
    def generate_daily_reading() -> dict:
        return {
            "lucky_numbers": FortuneTeller.generate_lucky_numbers(),
            "lucky_color": random.choice(LUCKY_COLORS),
            "lucky_element": random.choice(LUCKY_ELEMENTS),
            "power_animal": random.choice(POWER_ANIMALS),
            "tarot_card": random.choice(TAROT_CARDS),
            "fortune": FortuneTeller.get_fortune(),
            "cosmic_energy": random.randint(1, 100),
            "moon_phase": random.choice(["New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous",
                                          "Full Moon", "Waning Gibbous", "Last Quarter", "Waning Crescent"]),
        }

    def display_banner(self):
        banner = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║     ███╗   ███╗██╗   ██╗███████╗████████╗██╗ ██████╗ █████╗ ██╗              ║
║     ████╗ ████║╚██╗ ██╔╝██╔════╝╚══██╔══╝██║██╔════╝██╔══██╗██║              ║
║     ██╔████╔██║ ╚████╔╝ ███████╗   ██║   ██║██║     ███████║██║              ║
║     ██║╚██╔╝██║  ╚██╔╝  ╚════██║   ██║   ██║██║     ██╔══██║██║              ║
║     ██║ ╚═╝ ██║   ██║   ███████║   ██║   ██║╚██████╗██║  ██║███████╗         ║
║     ╚═╝     ╚═╝   ╚═╝   ╚══════╝   ╚═╝   ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝         ║
║                                                                              ║
║            ███████╗ ██████╗ ██████╗ ████████╗██╗   ██╗███╗   ██╗███████╗     ║
║            ██╔════╝██╔═══██╗██╔══██╗╚══██╔══╝██║   ██║████╗  ██║██╔════╝     ║
║            █████╗  ██║   ██║██████╔╝   ██║   ██║   ██║██╔██╗ ██║█████╗       ║
║            ██╔══╝  ██║   ██║██╔══██╗   ██║   ██║   ██║██║╚██╗██║██╔══╝       ║
║            ██║     ╚██████╔╝██║  ██║   ██║   ╚██████╔╝██║ ╚████║███████╗     ║
║            ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚══════╝     ║
║                                                                              ║
║                    ████████╗███████╗██╗     ██╗     ███████╗██████╗          ║
║                    ╚══██╔══╝██╔════╝██║     ██║     ██╔════╝██╔══██╗         ║
║                       ██║   █████╗  ██║     ██║     █████╗  ██████╔╝         ║
║                       ██║   ██╔══╝  ██║     ██║     ██╔══╝  ██╔══██╗         ║
║                       ██║   ███████╗███████╗███████╗███████╗██║  ██║         ║
║                       ╚═╝   ╚══════╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝         ║
║                                                                              ║
║                           ✨ Version 3000 ✨                                 ║
║                     🔮 Peer Into Your Destiny 🔮                             ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """
        print(banner)

    def display_menu(self):
        menu = """
┌─────────────────────────────────────────────────────────────────────────────┐
│                              MAIN MENU                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│   [1] 🎲 Get Lucky Numbers          [5] 🌙 Moon & Cosmic Energy             │
│   [2] 🔮 Daily Fortune Reading      [6] 📜 View Fortune History             │
│   [3] ♈ Zodiac Reading             [7] 🎴 Draw Tarot Card                  │
│   [4] 🌟 Complete Mystical Reading  [8] ❌ Exit                             │
└─────────────────────────────────────────────────────────────────────────────┘
        """
        print(menu)

    def run_lucky_numbers(self):
        print("\n" + "═" * 50)
        print("          🎲 LUCKY NUMBERS GENERATOR 🎲")
        print("═" * 50)
        numbers = self.generate_lucky_numbers()
        print(f"\n  Your lucky numbers are: {' - '.join(map(str, numbers))}")
        print(f"\n  Bonus number: {random.randint(1, 10)}")
        print("\n" + "═" * 50)

    def run_daily_fortune(self):
        print("\n" + "═" * 50)
        print("           🔮 DAILY FORTUNE READING 🔮")
        print("═" * 50)
        category, fortune = self.get_fortune()
        print(f"\n  Category: {category.upper()}")
        print(f"\n  \"{fortune}\"")
        print("\n" + "═" * 50)

    def run_zodiac_reading(self):
        print("\n" + "═" * 50)
        print("            ♈ ZODIAC READING ♈")
        print("═" * 50)
        print("\n  Available signs:", ", ".join([s.capitalize() for s in ZODIAC_SIGNS.keys()]))
        sign = input("\n  Enter your zodiac sign: ").strip()
        reading = self.get_zodiac_reading(sign)
        if reading:
            print(f"\n  {reading['symbol']} {reading['sign']} ({reading['dates']})")
            print(f"  Element: {reading['element']}")
            print(f"  Lucky Day: {reading['lucky_day']}")
            print(f"  Best Compatibility: {reading['compatibility']}")
            print(f"  Today's Mood: {reading['mood']}")
        else:
            print("\n  ⚠️  Invalid zodiac sign. Please try again.")
        print("\n" + "═" * 50)

    def run_complete_reading(self):
        print("\n" + "═" * 70)
        print("              🌟 COMPLETE MYSTICAL READING 🌟")
        print("═" * 70)
        reading = self.generate_daily_reading()
        self._record_session(reading)

        print(f"\n  📅 Date: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}")
        print(f"\n  🎲 Lucky Numbers: {' - '.join(map(str, reading['lucky_numbers']))}")
        print(f"  🎨 Lucky Color: {reading['lucky_color']}")
        print(f"  🌍 Lucky Element: {reading['lucky_element']}")
        print(f"  🦅 Power Animal: {reading['power_animal']}")
        print(f"  🎴 Tarot Card: {reading['tarot_card']}")
        print(f"  🌙 Moon Phase: {reading['moon_phase']}")
        print(f"  ⚡ Cosmic Energy Level: {reading['cosmic_energy']}%")

        cat, fortune = reading['fortune']
        print(f"\n  💫 Fortune ({cat.capitalize()}):")
        print(f"     \"{fortune}\"")

        print("\n" + "═" * 70)

    def run_cosmic_energy(self):
        print("\n" + "═" * 50)
        print("          🌙 MOON & COSMIC ENERGY 🌙")
        print("═" * 50)
        phases = ["🌑", "🌒", "🌓", "🌔", "🌕", "🌖", "🌗", "🌘"]
        phase_name = random.choice(["New Moon", "Waxing Crescent", "First Quarter",
                                     "Waxing Gibbous", "Full Moon", "Waning Gibbous",
                                     "Last Quarter", "Waning Crescent"])
        energy = random.randint(1, 100)
        energy_bar = "█" * (energy // 5) + "░" * (20 - energy // 5)

        print(f"\n  Moon Phase: {random.choice(phases)} {phase_name}")
        print(f"\n  Cosmic Energy: [{energy_bar}] {energy}%")
        print(f"\n  Spiritual Alignment: {random.choice(['Strong', 'Moderate', 'Building', 'Peak'])}")
        print("\n" + "═" * 50)

    def run_view_history(self):
        print("\n" + "═" * 50)
        print("           📜 FORTUNE HISTORY 📜")
        print("═" * 50)
        print(f"\n  Total readings: {self.history['total_fortunes']}")
        if self.history['sessions']:
            print(f"  Last reading: {self.history['sessions'][-1]['timestamp'][:10]}")
            recent = self.history['sessions'][-3:]
            print("\n  Recent sessions:")
            for session in reversed(recent):
                print(f"    • {session['timestamp'][:16].replace('T', ' ')}")
        else:
            print("\n  No fortune history yet. Get a complete reading!")
        print("\n" + "═" * 50)

    def run_tarot(self):
        print("\n" + "═" * 50)
        print("            🎴 TAROT CARD DRAW 🎴")
        print("═" * 50)
        card = random.choice(TAROT_CARDS)
        reversed_card = random.choice([True, False])
        orientation = "(Reversed)" if reversed_card else "(Upright)"

        print(f"\n  You drew: {card} {orientation}")
        print("\n  " + "┌" + "─" * 20 + "┐")
        print("  │" + card.center(20) + "│")
        print("  " + "└" + "─" * 20 + "┘")
        print("\n" + "═" * 50)

    def run(self):
        self.display_banner()
        print(f"\n  {self.get_greeting()}! The spirits have been expecting you...")
        print(f"  Today is {datetime.now().strftime('%A, %B %d, %Y')}\n")

        while True:
            self.display_menu()
            choice = input("  Enter your choice (1-8): ").strip()

            if choice == "1":
                self.run_lucky_numbers()
            elif choice == "2":
                self.run_daily_fortune()
            elif choice == "3":
                self.run_zodiac_reading()
            elif choice == "4":
                self.run_complete_reading()
            elif choice == "5":
                self.run_cosmic_energy()
            elif choice == "6":
                self.run_view_history()
            elif choice == "7":
                self.run_tarot()
            elif choice == "8":
                print("\n  ✨ May the stars guide your path! Farewell, seeker... ✨\n")
                break
            else:
                print("\n  ⚠️  Invalid choice. Please select 1-8.\n")

            input("\n  Press Enter to continue...")


if __name__ == "__main__":
    teller = FortuneTeller()
    teller.run()
    print("go to heaven")
