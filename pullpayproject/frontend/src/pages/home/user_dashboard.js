// src/components/UserDashboard.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function UserDashboard() {
    const [userData, setUserData] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        const token = localStorage.getItem('authToken');

        if (!token) {
            setError("No authentication token found. Please log in.");
            return;
        }

        axios.get('http://localhost:8000/api/user-dashboard/', {
            headers: {
                Authorization: `Bearer ${token}`,
            },
            withCredentials: true,
        })
            .then((response) => {
                setUserData(response.data);
            })
            .catch((error) => {
                console.error("Error fetching user data:", error);
                setError("Failed to fetch user data. Please ensure you are logged in.");
            });
    }, []);

    if (error) {
        return <div>{error}</div>;
    }

    if (!userData) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h1>User Dashboard</h1>
            <p>Username: {userData.user_first_name}</p>
            <p>Email: {userData.email}</p>
        </div>
    );
}

export default UserDashboard;
