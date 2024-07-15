import json
import os
import tkinter as tk

SCRIPT_PATH = os.path.abspath(__file__)
LAB_DIR_PATH = os.path.join(os.path.dirname(os.path.dirname(SCRIPT_PATH)), "out")

class LabyrinthMap():
    def __init__(self, root, background="black", width=1000, height=300):
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
            self.plot(tier)
        else:
            print("Please select a valid labyrinth tier.")

    def get_lab_dicts(self):
        try:
            all_lab_data = {}
            for lab_file in os.listdir(LAB_DIR_PATH):
                with open(os.path.join(LAB_DIR_PATH, lab_file), 'r', encoding="utf-8") as f:
                    data = json.load(f)[0]
                    lab_tier = data.pop('difficulty')
                    all_lab_data[lab_tier] = data
            return all_lab_data
        except Exception as e:
            print(f"Error loading labyrinth data: {e}")
            return {}

    def plot(self, lab_tier, r=20):
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
            "exits": list(room["exits"].values()) if "exits" in room else [],
            "out": list(room["exits"].keys()) if "exits" in room else [],
            "center": coords(room)
        } for room in rooms]

        all_room_data.sort(key=lambda x: x["id"])  # Sort the list after it's created

        # Construct paths in a more concise way
        paths = [{
            "id": room["id"],
            "color": "#e2be2d" if room.get("trial") else "#00a86b",
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
            # ex = tuple(zip(room["out"], room["exits"]))
            
            a = [(*room["center"], *door) for door in room["doors"]]
            arrows.extend(a)
            for co, e in list(zip(a, room["out"])):
                c = list(co)
                if e == "N":
                    c[1] -= r
                elif e == "NE":
                    c[1] -= r-(r/4)
                    c[0] += r-(r/4)
                elif e == "NW":
                    c[1] -= r-(r/4)
                    c[0] -= r-(r/4)
                elif e == "E":
                    c[1] += r-(r/4)
                    c[0] -= r-(r/4)
                exits.append(tuple(c))

            plot_circles.append((*room["center"], r, room["color"], room["outline"]))
            # exits.append()

        # print(exits)

        # Determine arrow colors
        plot_arrows = []
        for idx, arrow in enumerate(arrows):
            arrow_coords = arrow[:4]
            fill = '#FFFFFF'
            # if tuple(sorted(arrow_coords)) in dupes:
            #     fill = '#6a6e6a'
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
                # print(path)
                return path

            # Explore neighbors
            for neighbor in rooms[current]['exits']:
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append((neighbor, new_path))
            
            print(path)

        return "No valid path found"

    def _circle(self, x, y, r, fill, outline):
    
        return self.canvas.create_oval(x - r, y - r,
                                        x + r, y + r, 
                                        fill=fill, outline=outline, width=4)
    
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

if __name__ == "__main__":
    root = tk.Tk()
    root.title("The Lord's Labyrinth")
    root.geometry("1200x400")

    LabyrinthMap(root)
    root.mainloop()
