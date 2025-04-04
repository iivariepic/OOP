import random
import tkinter as tk
import math

from django.urls import is_valid_path


def haversine(lat1, lon1, lat2, lon2):
    """Calculates the distance between two points in kilometers using the Haversine formula."""
    R = 6371  # Earth's radius in kilometers
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c

class Transition:
    def __init__(self, target_vertex, weight):
        self.__target = target_vertex  # Private instance variable
        self.__weight = weight        # Private instance variable

    @property
    def target(self):
        return self.__target

    @property
    def weight(self):
        return self.__weight

class Vertex:
    def __init__(self, name, x, y):
        self.__name = name            # Private instance variable
        self.__x = x                  # X-coordinate (latitude)
        self.__y = y                  # Y-coordinate (longitude)
        self.__transitions = []       # Private list of Transition objects

    @property
    def name(self):
        return self.__name

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def transitions(self):
        return self.__transitions

    def add_transition(self, target_vertex, weight):
        self.__transitions.append(Transition(target_vertex, weight))

class Graph:
    def __init__(self):
        self.__vertices = {}          # Private dictionary for Vertex objects

    def add_vertex(self, vertex):
        assert vertex.name not in self.__vertices, "Vertex already exists in the graph"
        self.__vertices[vertex.name] = vertex

    def add_edge(self, vertex1_name, vertex2_name, weight):
        assert vertex1_name in self.__vertices and vertex2_name in self.__vertices, "Vertices must exist in the graph"
        vertex1 = self.__vertices[vertex1_name]
        vertex2 = self.__vertices[vertex2_name]
        vertex1.add_transition(vertex2, weight)

    def get_vertices(self):
        return list(self.__vertices.keys())

    def get_edges(self):
        edges = []
        for vertex in self.__vertices.values():
            for transition in vertex.transitions:
                edges.append((vertex.name, transition.target.name, transition.weight))
        return edges

    def get_vertex_positions(self):
        """Returns the coordinates of all vertices as a dictionary."""
        return {vertex.name: (vertex.x, vertex.y) for vertex in self.__vertices.values()}


    def is_valid_path(self, city_names):
        """
        Checks if the given list of city names forms a valid path in the graph.
        :param city_names: List of city names representing the path.
        :return: True if the path is valid, False otherwise.
        """
        for i in range(len(city_names) - 1):
            current_city = city_names[i]
            next_city = city_names[i + 1]

            # Ensure both cities exist in the graph
            if current_city not in self.__vertices or next_city not in self.__vertices:
                return False

            # Check if there is a direct transition between the current and next city
            current_vertex = self.__vertices[current_city]
            if not any(transition.target.name == next_city for transition in current_vertex.transitions):
                return False

        return True


    def get_path_cost(self, path):

        if not self.is_valid_path(path):
            return None

        total_cost = 0.0
        for i in range(len(path) - 1):
            current_vertex = self.__vertices[path[i]]
            next_city = path[i + 1]
            for transition in current_vertex.transitions:
                if transition.target.name == next_city:
                    total_cost += transition.weight
                    break
        return total_cost


class GraphPlotter:
    def __init__(self, graph, width, height, margin):
        self.graph = graph
        self.width = width
        self.height = height
        self.margin = margin

    def plot(self):
        # Create a tkinter window
        window = tk.Tk()
        window.title("Graph Plotter")

        # Define the canvas size
        canvas_width = self.width
        canvas_height = self.height
        canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="white")
        canvas.pack()

        # Get the coordinates of the graph's vertices
        vertex_positions = self.graph.get_vertex_positions()

        # Scale the coordinates to fit the canvas
        min_x = min(pos[1] for pos in vertex_positions.values())  # Longitude
        max_x = max(pos[1] for pos in vertex_positions.values())
        min_y = min(pos[0] for pos in vertex_positions.values())  # Latitude
        max_y = max(pos[0] for pos in vertex_positions.values())

        def scale(value, min_val, max_val, new_min, new_max):
            """Scales a value to a new range."""
            if max_val == min_val:  # Avoid division by zero
                return (new_min + new_max) / 2
            return new_min + (value - min_val) * (new_max - new_min) / (max_val - min_val)

        # Scale the city coordinates to fit the canvas and flip the y-coordinates
        scaled_positions = {
            vertex: (
                scale(x, min_x, max_x, self.margin, canvas_width - self.margin),
                scale(y, min_y, max_y, canvas_height - self.margin, self.margin)  # Flip the y-coordinate
            )
            for vertex, (y, x) in vertex_positions.items()  # Note: (y, x) order
        }

        # Draw the cities
        for vertex, (x, y) in scaled_positions.items():
            city_radius = 15
            canvas.create_oval(x - city_radius, y - city_radius, x + city_radius, y + city_radius, fill="lightblue")
            canvas.create_text(x, y, text=vertex, font=("Arial", 10))

        # Get the graph's edges
        edges = self.graph.get_edges()

        # Draw the edges and their weights
        for v1, v2, weight in edges:
            x1, y1 = scaled_positions[v1]
            x2, y2 = scaled_positions[v2]

            # Draw the edge
            canvas.create_line(x1, y1, x2, y2, fill="black")

            # Draw the weight in the middle of the edge
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            canvas.create_text(mid_x, mid_y, text=f"{weight:.1f} km", font=("Arial", 8), fill="red")

        # Show the tkinter window
        window.mainloop()


# Create the graph
graph = Graph()

# Add vertices to the graph using the coordinates list
coordinates = [
    ("Turku", (60.4518, 22.2666)),
    ("Salo", (60.3833, 23.1333)),
    ("Helsinki", (60.1695, 24.9354)),
    ("Tampere", (61.4991, 23.7871)),
    ("Pori", (61.4850, 21.7972)),
    ("Rauma", (61.1272, 21.5113)),
    ("Lahti", (60.9827, 25.6615)),
    ("Kuopio", (62.8924, 27.6770)),
    ("Jyväskylä", (62.2426, 25.7473)),
    ("Oulu", (65.0121, 25.4651)),
    ("Kuusamo", (65.9667, 29.1833)),
    ("Rovaniemi", (66.5039, 25.7294)),
    ("Kittilä", (67.6547, 24.9074)),
    ("Vaasa", (63.0960, 21.6158)),
    ("Kokkola", (63.8385, 23.1307)),
    ("Kajaani", (64.2250, 27.7333)),
    ("Kemi", (65.7361, 24.5633)),
    ("Kotka", (60.4664, 26.9458)),
    ("Lappeenranta", (61.0586, 28.1887)),
    ("Joensuu", (62.6010, 29.7634)),
    ("Mikkeli", (61.6886, 27.2724)),
    ("Savonlinna", (61.8688, 28.8864)),
    ("Espoo", (60.2055, 24.6559)),
    ("Vantaa", (60.2941, 25.0409)),
    ("Hyvinkää", (60.6336, 24.8585)),
    ("Porvoo", (60.3932, 25.6639)),
    ("Lohja", (60.2480, 24.0658)),
    ("Hämeenlinna", (60.9950, 24.4643)),
    ("Seinäjoki", (62.7903, 22.8403)),
    ("Kouvola", (60.8681, 26.7042)),
    ("Imatra", (61.1700, 28.7717)),
    ("Raahe", (64.6833, 24.4833))
]

for name, (x, y) in coordinates:
    graph.add_vertex(Vertex(name, x, y))

# Add edges to the graph using the Haversine formula
vertices = graph.get_vertices()
num_edges = 80  # Number of edges to add
added_edges = 0

random.seed(11)  # Set the random seed for reproducibility
while added_edges < num_edges:
    v1_name, v2_name = random.sample(vertices, 2)
    v1 = graph.get_vertex_positions()[v1_name]
    v2 = graph.get_vertex_positions()[v2_name]

    # Calculate the Haversine distance
    weight = haversine(v1[0], v1[1], v2[0], v2[1])
    graph.add_edge(v1_name, v2_name, weight)
    added_edges += 1



# Test the is_valid_path method
print("Testing is_valid_path method...")

# Valid paths
valid_path_1 = ["Kuusamo", "Kittilä", "Kajaani", "Vaasa" ]
valid_path_2 = ["Lohja", "Vaasa"]

# Invalid paths
invalid_path_1 = ["Vaasa", "Lohja"]  # No direct connection between Turku and Kuopio
invalid_path_2 = ["Espoo", "Rovaniemi", "Kittilä"]  # No direct connection between Espoo and Rovaniemi

# Test the method
print(f"Path {valid_path_1} is valid: {graph.is_valid_path(valid_path_1)}")  # Expected: True
print(f"Path {valid_path_2} is valid: {graph.is_valid_path(valid_path_2)}")  # Expected: True
print(f"Path {invalid_path_1} is valid: {graph.is_valid_path(invalid_path_1)}")  # Expected: False
print(f"Path {invalid_path_2} is valid: {graph.is_valid_path(invalid_path_2)}")  # Expected: False

# Test the travel cost
print("Path cost for", valid_path_1, ":", graph.get_path_cost(valid_path_1))
print("Path cost for", invalid_path_2, ":", graph.get_path_cost(invalid_path_2))

# Plot the graph
plotter = GraphPlotter(graph, width=600, height=800, margin=50)
plotter.plot()

