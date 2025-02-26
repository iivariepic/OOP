class WeatherStation:
    def __init__(self, name:str):
        self.name:str = name
        self.observations:list[str] = []

    def add_observation(self, observation:str):
        self.observations.append(observation)

    def latest_observation(self):
        return self.observations[-1]

    def number_of_observations(self):
        return len(self.observations)

    def __str__(self):
        return f"{self.name}, {len(self.observations)} observations"

def main():
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())
    station.add_observation("Thunderstorm")
    print(station.latest_observation())
    print(station.number_of_observations())
    print(station)

if __name__ == "__main__":
    main()
