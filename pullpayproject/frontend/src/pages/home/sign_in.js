import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "./sign_in.css";

export default function SignIn() {
    const {
        register,
        handleSubmit,
        formState: { errors },
    } = useForm();
    const navigate = useNavigate(); // useNavigate hook for redirection

    const onSubmit = async (data) => {
        try {
            const response = await axios.post("http://localhost:8000/api/login/", data);
            console.log("Login successful:", response.data);

            // Redirect to dashboard or another page on successful login
            navigate("/dashboard"); // Change "/dashboard" to the desired route
        } catch (error) {
            console.error("Login failed:", error);
            if (error.response) {
                alert(error.response.data.error || "Login failed. Please try again.");
            } else {
                alert("An unexpected error occurred.");
            }
        }
    };

    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            {/* Username */}
            <input
                placeholder="Username"
                {...register("username", { required: true })}
            />
            {errors.username && <span>This field is required</span>}

            {/* Password */}
            <input
                type="password"
                placeholder="Password"
                {...register("password", { required: true })}
            />
            {errors.password && <span>This field is required</span>}

            {/* Submit Button */}
            <input type="submit" value="Sign In" />
        </form>
    );
}