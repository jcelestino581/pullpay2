import { useForm } from "react-hook-form"
import "./register.css";
import axios from "axios";

export default function Register() {
    const {
        register,
        handleSubmit,
        formState: { errors },
    } = useForm();

    const onSubmit = async (data) => {
        try {
            const response = await axios.post("http://localhost:8000/api/register/", data);
            console.log("Registration successful:", response.data);
            // Handle successful registration (e.g., navigate or show a success message)
        } catch (error) {
            console.error("Registration failed:", error);
            if (error.response) {
                if (error.response.data.email) {
                    alert("This email is already registered.");
                } else {
                    alert("Registration failed. Please try again.");
                }
            } else {
                alert("An unexpected error occurred.");
            }
        }
    };

    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            {/* First Name */}
            <input
                placeholder="First Name"
                {...register("user_first_name", { required: true })}
            />
            {errors.user_first_name && <span>This field is required</span>}

            {/* Last Name */}
            <input
                placeholder="Last Name"
                {...register("user_last_name", { required: true })}
            />
            {errors.user_last_name && <span>This field is required</span>}

            {/* Email */}
            <input
                type="email"
                placeholder="Email"
                {...register("email", { required: true })}
            />
            {errors.email && <span>This field is required</span>}

            {/* Phone Number (optional) */}
            <input
                placeholder="Phone Number (optional)"
                {...register("phone_number")}
            />

            {/* Address (optional) */}
            <input
                placeholder="Address (optional)"
                {...register("address")}
            />

            {/* Payment Method (optional) */}
            <input
                placeholder="Payment Method (optional)"
                {...register("payment_method")}
            />

            {/* Password */}
            <input
                type="password"
                placeholder="Password"
                {...register("password", { required: true })}
            />
            {errors.password && <span>This field is required</span>}

            {/* Submit Button */}
            <input type="submit" />
        </form>
    );
}