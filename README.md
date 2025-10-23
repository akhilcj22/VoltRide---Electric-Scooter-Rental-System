# 🚀 VoltRide - Electric Scooter Rental Management System

A comprehensive Django-based web application that simulates real-world electric scooter sharing services like Lime, Bird, or Spin. Built with modern web technologies and responsive design principles.

![Django](https://img.shields.io/badge/Django-5.1.2-green.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-purple.svg)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightblue.svg)

## 🌟 Features

### 👤 User Features
- **User Authentication** - Secure registration and login system
- **Scooter Browsing** - View available scooters with images and battery levels
- **Ride Management** - Start and end rides with automatic cost calculation
- **Ride History** - Track all past rides with duration and cost details
- **Real-time Status** - Live updates on scooter availability

### 🔧 Admin Features
- **Fleet Management** - Add, edit, and delete scooters
- **Image Upload** - Upload and manage scooter images
- **Dashboard Analytics** - System statistics and fleet overview
- **User Management** - Monitor user activities and ride data

### 💰 Business Logic
- **Smart Pricing** - Automatic cost calculation (₹30 per minute)
- **Ride Validation** - Prevents multiple simultaneous rides per user
- **Battery Tracking** - Monitor scooter battery levels
- **Availability Management** - Real-time scooter status updates

## 🛠️ Tech Stack

- **Backend**: Django 5.1.2, Python
- **Database**: SQLite
- **Frontend**: Bootstrap 5.3.0, HTML5, CSS3
- **Icons**: Font Awesome 6.0.0
- **File Handling**: Django Media Files
- **Authentication**: Django Built-in User System

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/VoltRide.git
   cd VoltRide
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   pip install pillow  # For image handling
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000`
   - Admin panel: `http://127.0.0.1:8000/admin`

## 🚀 Usage

### For Regular Users
1. **Register** a new account or **login** with existing credentials
2. **Browse available scooters** on the main page
3. **Click "Start Ride"** on any available scooter
4. **Confirm your ride** on the detailed scooter page
5. **End your ride** when finished from the ride history page
6. **View your ride history** and costs

### For Administrators
1. **Login** with admin credentials
2. **Access Admin Dashboard** to view system statistics
3. **Manage Fleet** - Add, edit, or delete scooters
4. **Upload Images** for scooters
5. **Monitor System** - Track active rides and user activities

## 📱 Screenshots

### Main Dashboard
- Responsive card-based layout
- Real-time scooter availability
- Battery level indicators
- Professional image display

### Ride Management
- Detailed scooter information
- Cost calculation preview
- Smooth user experience flow

### Admin Panel
- Comprehensive fleet management
- System analytics dashboard
- User activity monitoring

## 🏗️ Project Structure

```
VoltRide/
├── manage.py
├── db.sqlite3
├── media/                    # Uploaded images
├── static/                   # Static files
├── templates/               # Base templates
├── VoltRide/                # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/                   # User authentication app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── templates/
└── scooters/                # Main application
    ├── models.py
    ├── views.py
    ├── forms.py
    ├── urls.py
    └── templates/
        └── scooters/
```

## 🎯 Key Models

### Scooter Model
- `name` - Scooter name
- `identifier` - Unique scooter ID
- `is_available` - Availability status
- `battery_level` - Battery percentage
- `image` - Scooter image
- `created_at` - Creation timestamp

### Ride Model
- `user` - Foreign key to User
- `scooter` - Foreign key to Scooter
- `start_time` - Ride start timestamp
- `end_time` - Ride end timestamp
- `cost` - Calculated ride cost

## 🔒 Security Features

- **CSRF Protection** - Cross-site request forgery protection
- **User Authentication** - Secure login/logout system
- **Role-based Access** - Admin and user permissions
- **Input Validation** - Form validation and sanitization
- **File Upload Security** - Secure image upload handling

## 📊 Business Logic

### Cost Calculation
- **Rate**: ₹30 per minute
- **Automatic calculation** when ride ends
- **Real-time cost preview** before starting ride

### Ride Management
- **Single ride per user** - Prevents multiple simultaneous rides
- **Automatic status updates** - Scooter availability management
- **Duration tracking** - Precise ride time calculation

## 🎨 Design Features

### Responsive Design
- **Mobile-first approach** with Bootstrap 5
- **Card-based layout** for better user experience
- **Touch-friendly interface** for mobile devices
- **Professional styling** with custom CSS

### User Experience
- **Intuitive navigation** with clear visual hierarchy
- **Real-time feedback** with success/error messages
- **Smooth animations** and hover effects
- **Accessibility features** with proper ARIA labels

## 🚀 Deployment

### Production Considerations
- Update `DEBUG = False` in settings.py
- Configure proper database (PostgreSQL recommended)
- Set up static file serving
- Configure media file handling
- Set up proper security settings

### Environment Variables
```python
SECRET_KEY = 'your-secret-key'
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn Profile](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap Team for the amazing CSS framework
- Font Awesome for the beautiful icons
- The open-source community for inspiration

---

⭐ **Star this repository if you found it helpful!**

## 📈 Future Enhancements

- [ ] Payment integration
- [ ] GPS tracking
- [ ] Push notifications
- [ ] Mobile app development
- [ ] Advanced analytics
- [ ] Multi-language support
- [ ] API development
- [ ] Real-time chat support

---

**Built with ❤️ using Django and modern web technologies**
