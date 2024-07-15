import json
import os
import tkinter as tk
import math
import subprocess

from datetime import datetime, timezone

SCRIPT_PATH = os.path.abspath(__file__)
TSC_PATH = os.path.join(os.path.dirname(os.path.dirname(SCRIPT_PATH)), "sherpa", "tsc")
LAB_DIR_PATH = os.path.join(TSC_PATH, "out")

LAB_TYPES = ["Normal", "Cruel", "Merciless", "Uber"]

def current_date():
    return datetime.now(timezone.utc)

def fetch_data():

    p = "%Y-%m-%d %H:%M:%S"

    lab_data = get_lab_dicts()
    if lab_data:
        # check if data is up-to-date
        now_utc = current_date()
        pull_date = lab_data["date"]

        if datetime.strptime(pull_date, p).date() != now_utc.date():
            print("Date does not match, fetching data")

            cwd = os.getcwd()
            os.chdir(TSC_PATH)

            # call tsc to redo 
            result = subprocess.run([os.path.join(TSC_PATH, "start.bat")], capture_output=True, text=True)
            # Print the output and error (if any)
            # print('stdout:\n', result.stdout)                                     # TODO send to debug
            print('stderr:\n', result.stderr)

            os.chdir(cwd)

            lab_data = get_lab_dicts()
        else:
            print("Dates match, using existing data")

    # print(json.dumps(lab_data, indent = 4))
    
    return lab_data

def get_lab_dicts():

    data = {}

    try:
        with open(os.path.join(LAB_DIR_PATH, "compass.json"), 'r', encoding="utf-8") as f:
            data = json.load(f)

    except Exception as e:
        print(f"Error loading labyrinth data: {e}")

    return data

def room_color(room):
    if room.get("name") == "aspirant's trial":
        return "#45b6fe"
    if "golden-door" in room.get("contents"):
        return "#e2be2d"
    if "silver-door" in room.get("contents"):
        return "#b5b7bb"
    return "#00a86b"

def is_key(room):
    if "golden-key" in room.get("contents"):
        return "gold"
    if "silver-key" in room.get("contents"):
        return "silver"
    return ""

def clean_data():
    
    cleaned = {}

    lab_data = fetch_data()

    izaro = ["weapon", "phase1", "phase2", "trap1", "trap2"]
    drop_room_keys = ["dangerous", "content_directions"]

    for lab in LAB_TYPES:
        cleaned[lab] = {}
        cleaned[lab]["graph"] = {}

        lab_dict = lab_data[lab]
        
        cleaned[lab]["Izaro"] = {i:lab_dict[i] for i in izaro}
        
        cleaned[lab]["rooms"] = {}
        for room in lab_dict["rooms"]:
            for k in drop_room_keys:
                room.pop(k)
            
            id = room.pop("id")
            
            exits = room.pop("exits") 
            cleaned[lab]["graph"][id] = list(exits.items()) 
            print(cleaned[lab]["graph"][id])
            # cleaned[lab]["graph"][id] = list(exits.values()) 
            
            room["loc"] = (room.pop("x"), room.pop("y"))

            cleaned[lab]["color"][id] = room_color(room) 
            cleaned[lab]["outline"][id] = "#743aad" if "darkshrine" in room["contents"] else "#7f7f7f"
            cleaned[lab]["rooms"][id] = room 

    return cleaned

class LabyrinthMap():
    def __init__(self, root, r=20, background="black", width=1000, height=300):
        self.r = r
        self.root = root
        self.canvas = tk.Canvas(self.root, width=width, height=height, 
                                borderwidth=0, highlightthickness=0, 
                                bg=background)
        self.canvas.pack()

        self.var = tk.StringVar(self.root)
        self.var.set("Choose Labyrinth Tier")
        options = ["Normal", "Cruel", "Merciless", "Uber"]
        self.option_menu = tk.OptionMenu(self.root, self.var, *options)
        self.option_menu.pack(pady=10)

        self.select = tk.Button(self.root, text="Select", command=self.on_select)
        self.select.pack()

    def on_select(self):
        tier = self.var.get()
        if tier in ["Normal", "Cruel", "Merciless", "Uber"]:
            self.plot(tier, self.r)
        else:
            print("Please select a valid labyrinth tier.")

    def get_lab_dicts(self):
        try:
            with open(os.path.join(LAB_DIR_PATH, "compass.json"), 'r', encoding="utf-8") as f:
                return json.load(f)
        
        except Exception as e:
            print(f"Error loading labyrinth data: {e}")
            return {}

    def plot(self, lab_tier, r):
        lab_data = self.get_lab_dicts()
        if lab_tier not in lab_data:
            print(f"Labyrinth tier '{lab_tier}' not found.")
            return

        self.canvas.delete("all")
        rooms = lab_data[lab_tier]["rooms"]
        plot_arrows, plot_circles = self._plot(rooms, r)
        
        for circle in plot_circles:
            self._circle(*circle)
        for arrow in plot_arrows:
            self._arrow(*arrow)

    def _plot(self, rooms, r):
        def coords(room):
            return int(room["x"]), int(room["y"])  # Simplify the coordinate extraction

        # Combine room data construction into a single list comprehension for efficiency
        room_coords = dict((int(room["id"]),coords(room)) for room in rooms)

        all_room_data = [{
            "id": int(room["id"]),
            "name": room["name"],
            "trial": room.get("name") == "aspirant's trial",
            "darkshrine?": "darkshrine" in room["contents"],
            "contents": room["contents"],
            "exits": list(room["exits"].values()) if "exits" in room else [],
            "out": list(room["exits"].keys()) if "exits" in room else [],
            "center": coords(room)
        } for room in rooms]

        all_room_data.sort(key=lambda x: x["id"])  # Sort the list after it's created

        def color(room):
            if room.get("trial"):
                return "#45b6fe"
            if "golden-door" in room.get("contents"):
                return "#e2be2d"
            if "silver-door" in room.get("contents"):
                return "#b5b7bb"
            return "#00a86b"
        
        def key(room):
            if "golden-key" in room.get("contents"):
                return "gold"
            if "silver-key" in room.get("contents"):
                return "silver"
            return ""

        # Construct paths in a more concise way
        paths = [{
            "id": room["id"],
            "color": color(room),
            "key": key(room),
            "argus": True if "argus" in room.get("contents") else False,
            "required": True if room.get("trial") else False,
            "center": room["center"],
            "outline": "#743aad" if room["darkshrine?"] else "#7f7f7f",
            "out": room["out"],
            "exits": list(map(int, room["exits"])),
            "doors": [all_room_data[int(idx)-1]["center"] for idx in room["exits"]]
        } for room in all_room_data]

        shortest = dict((room["id"], {"exits": room["exits"], "required": room["required"]}) for room in paths)
        shortest_path = self.find_shortest_path_with_requirements(shortest)
        shortest_path = [(*room_coords[shortest_path[i]], *room_coords[shortest_path[i+1]]) for i in range(len(shortest_path) - 1)]

        arrows = []
        plot_circles = []
        exits = []
        for room in paths:
            a = [(*room["center"], *door) for door in room["doors"]]
            arrows.extend(a)
            for co, e in list(zip(a, room["out"])):
                c = list(co)
                if e not in ["N", "NE", "NW", "E", "SE", "C"]:
                    print(f"Direction '{e}' not accounted for")
                if e == "N":
                    c[1] -= r
                elif e == "NE":
                    c[1] -= r-(r/4)
                    c[0] += r-(r/4)
                elif e == "SE":
                    c[0] += r-(r/4)
                    c[1] += r-(r/4)
                elif e == "NW":
                    c[1] -= r-(r/4)
                    c[0] -= r-(r/4)
                elif e == "E":
                    c[1] += r-(r/4)
                    c[0] -= r-(r/4)
                exits.append(tuple(c))

            plot_circles.append((*room["center"], r, room["color"], room["outline"], room["key"], room["argus"]))

        # Determine arrow colors
        plot_arrows = []
        for idx, arrow in enumerate(arrows):
            arrow_coords = arrow[:4]
            fill = '#FFFFFF'
            if arrow_coords in shortest_path:
                fill = "blue"
            plot_arrows.append((*exits[idx][:4], fill))

        return plot_arrows, plot_circles

    def find_shortest_path_with_requirements(self, rooms, start=1):

        # Extract required rooms
        required_rooms = {room for room, properties in rooms.items() if properties.get('required')}
        end = max(required_rooms)
        # Initialize BFS
        queue = [(start, [start])]
        visited = set()

        while queue:
            (current, path) = queue.pop(0)
            visited.add(current)

            # Check if the current path includes all required rooms and is at the end
            if current == end and required_rooms.issubset(set(path)):
                return path

            # Explore neighbors
            for neighbor in rooms[current]['exits']:
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append((neighbor, new_path))


        return "No valid path found"

    def create_triangle(self, x, y, radius):
        points = []
        for i in range(3):
            angle = math.radians(90 + i * 120)  # Starting from the top (90 degrees)
            point_x = x + radius * math.cos(angle)
            point_y = y + radius * math.sin(angle)
            points.extend([point_x, point_y])
        return points

    def _circle(self, x, y, r, fill, outline, key, argus):
        self.canvas.create_oval(x - r, y - r,
                                        x + r, y + r, 
                                        fill=fill, outline=outline, width=4)
        if key:
            pts = self.create_triangle(x,y,r)
            if key == "silver":
                self.canvas.create_polygon(pts, fill="#b5b7bb")
            else:
                self.canvas.create_polygon(pts, fill="#e2be2d")
        
        if argus: 
            self.canvas.create_oval(x - r/3, y - r/3,
                                x + r/3, y + r/3, 
                                fill="orange", outline=outline, width=2)

    def _arrow(self, x0, y0, x1, y1, fill):
        """
        Draws an arrow between two points on the provided canvas.

        Parameters:
        x0, y0 (int): Starting coordinates of the arrow.
        x1, y1 (int): Ending coordinates of the arrow.
        canvas (tk.Canvas): The canvas on which to draw the arrow.

        Returns:
        The ID of the created arrow.
        """
        arrow_options = {
        'arrow': tk.LAST, 
        'fill': fill,              # Bright color for better contrast
        'width': 3,                     # Wider line for better visibility
        'arrowshape': (10, 12, 4),      # Larger arrowhead
        'smooth': True                  # Enable smoothing
        }
        r_small = 3
        self.canvas.create_oval(x0 - r_small, y0 - r_small,
                            x0 + r_small, y0 + r_small, 
                            fill=fill, outline=fill, width=4)

        return self.canvas.create_line(x0, y0, x1, y1, **arrow_options)

    def get_duplicates(self, arrows):
        # Find duplicates using a set comprehension
        seen = set()
        dupes = set()
        for arrow in arrows:
            arrow_sorted = tuple(sorted(arrow[:4]))  # Consider only the coordinates for duplication check
            if arrow_sorted in seen:
                dupes.add(arrow_sorted)
            else:
                seen.add(arrow_sorted)
        return dupes

# if __name__ == "__main__":
#     # root = tk.Tk()
#     # root.title("The Lord's Labyrinth")
#     # root.geometry("1200x400")

#     # LabyrinthMap(root)
#     # root.mainloop()

#     main()
    
