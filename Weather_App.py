import tkinter as tk
from tkinter import ttk, messagebox
import requests
from datetime import datetime
import json

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App 🌤️")
        self.root.geometry("500x600")
        self.root.configure(bg='#87CEEB')  # Sky blue background
        
        
        self.API_KEY = "ad26703e8fbead132669bc346e7b0069"  # Replace with your actual API key
        self.BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
        
        self.setup_ui()
        
    def setup_ui(self):
        # Title Label
        title_label = tk.Label(
            self.root,
            text="🌍 Weather App 🌍",
            font=("Arial", 24, "bold"),
            bg='#87CEEB',
            fg='white'
        )
        title_label.pack(pady=20)
        
        # Search Frame
        search_frame = tk.Frame(self.root, bg='#87CEEB')
        search_frame.pack(pady=10)
        
        # City Entry
        self.city_entry = tk.Entry(
            search_frame,
            font=("Arial", 14),
            width=20,
            bd=2,
            relief="solid"
        )
        self.city_entry.pack(side=tk.LEFT, padx=5)
        self.city_entry.bind('<Return>', lambda event: self.get_weather())  # Enter key support
        
        # Search Button
        search_button = tk.Button(
            search_frame,
            text="Search 🔍",
            font=("Arial", 12, "bold"),
            bg='#4CAF50',
            fg='white',
            command=self.get_weather,
            cursor="hand2",
            bd=0,
            padx=15,
            pady=5
        )
        search_button.pack(side=tk.LEFT, padx=5)
        
        # Weather Display Frame
        self.weather_frame = tk.Frame(self.root, bg='white', relief="ridge", bd=2)
        self.weather_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # City Name Label
        self.city_label = tk.Label(
            self.weather_frame,
            text="Enter a city name",
            font=("Arial", 20, "bold"),
            bg='white',
            fg='#333'
        )
        self.city_label.pack(pady=10)
        
        # Temperature Label
        self.temp_label = tk.Label(
            self.weather_frame,
            text="",
            font=("Arial", 48, "bold"),
            bg='white',
            fg='#FF6B6B'
        )
        self.temp_label.pack(pady=5)
        
        # Weather Description
        self.desc_label = tk.Label(
            self.weather_frame,
            text="",
            font=("Arial", 16),
            bg='white',
            fg='#666'
        )
        self.desc_label.pack(pady=5)
        
        # Weather Icon (using emoji)
        self.icon_label = tk.Label(
            self.weather_frame,
            text="",
            font=("Arial", 64),
            bg='white'
        )
        self.icon_label.pack(pady=10)
        
        # Details Frame
        details_frame = tk.Frame(self.weather_frame, bg='white')
        details_frame.pack(pady=20)
        
        # Feels Like
        self.feels_label = tk.Label(
            details_frame,
            text="",
            font=("Arial", 12),
            bg='white',
            fg='#666'
        )
        self.feels_label.grid(row=0, column=0, padx=20, pady=5)
        
        # Humidity
        self.humidity_label = tk.Label(
            details_frame,
            text="",
            font=("Arial", 12),
            bg='white',
            fg='#666'
        )
        self.humidity_label.grid(row=0, column=1, padx=20, pady=5)
        
        # Wind Speed
        self.wind_label = tk.Label(
            details_frame,
            text="",
            font=("Arial", 12),
            bg='white',
            fg='#666'
        )
        self.wind_label.grid(row=1, column=0, padx=20, pady=5)
        
        # Pressure
        self.pressure_label = tk.Label(
            details_frame,
            text="",
            font=("Arial", 12),
            bg='white',
            fg='#666'
        )
        self.pressure_label.grid(row=1, column=1, padx=20, pady=5)
        
        # Last Updated
        self.update_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 10),
            bg='#87CEEB',
            fg='white'
        )
        self.update_label.pack(pady=5)
        
    def get_weather_icon(self, weather_main):
        """Return emoji based on weather condition"""
        weather_icons = {
            "Clear": "☀️",
            "Clouds": "☁️",
            "Rain": "🌧️",
            "Drizzle": "🌦️",
            "Thunderstorm": "⛈️",
            "Snow": "❄️",
            "Mist": "🌫️",
            "Fog": "🌫️",
            "Haze": "🌫️"
        }
        return weather_icons.get(weather_main, "🌡️")
    
    def get_weather(self):
        city = self.city_entry.get().strip()
        
        if not city:
            messagebox.showwarning("Warning", "Please enter a city name!")
            return
        
        try:
            # API call
            params = {
                'q': city,
                'appid': self.API_KEY,
                'units': 'metric'  # Use 'imperial' for Fahrenheit
            }
            
            response = requests.get(self.BASE_URL, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                self.display_weather(data)
            elif response.status_code == 404:
                messagebox.showerror("Error", "City not found! Please check the spelling.")
            elif response.status_code == 401:
                messagebox.showerror("Error", "Invalid API key! Please check your API key.")
            else:
                messagebox.showerror("Error", f"Error: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Network error: Please check your internet connection")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def display_weather(self, data):
        # Extract weather data
        city_name = data['name']
        country = data['sys']['country']
        temp = round(data['main']['temp'])
        feels_like = round(data['main']['feels_like'])
        description = data['weather'][0]['description'].capitalize()
        weather_main = data['weather'][0]['main']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        pressure = data['main']['pressure']
        
        # Update UI
        self.city_label.config(text=f"{city_name}, {country}")
        self.temp_label.config(text=f"{temp}°C")
        self.desc_label.config(text=description)
        self.icon_label.config(text=self.get_weather_icon(weather_main))
        
        self.feels_label.config(text=f"Feels like: {feels_like}°C")
        self.humidity_label.config(text=f"Humidity: {humidity}%")
        self.wind_label.config(text=f"Wind: {wind_speed} m/s")
        self.pressure_label.config(text=f"Pressure: {pressure} hPa")
        
        # Update timestamp
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.update_label.config(text=f"Last updated: {current_time}")
        
        # Change background color based on temperature
        if temp < 0:
            bg_color = '#E3F2FD'  # Very cold - light blue
        elif temp < 10:
            bg_color = '#BBDEFB'  # Cold - blue
        elif temp < 20:
            bg_color = '#90CAF9'  # Cool - medium blue
        elif temp < 30:
            bg_color = '#FFF9C4'  # Warm - light yellow
        else:
            bg_color = '#FFCCBC'  # Hot - light orange
            
        self.weather_frame.config(bg=bg_color)
        for widget in self.weather_frame.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(bg=bg_color)
            elif isinstance(widget, tk.Frame):
                widget.config(bg=bg_color)
                for child in widget.winfo_children():
                    child.config(bg=bg_color)

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    
    # Center the window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()

if __name__ == "__main__":
    main()