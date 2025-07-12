import axios from "axios";
//"http://localhost:8000/chat" | 
const BASE_URL = "https://edusync-1iju.onrender.com/chat";

export const sendMessage = async (message) => {
    return axios.post(BASE_URL, { message });
};
