import axios from "axios";

const BASE_URL = "http://localhost:8000/chat";

export const sendMessage = async (message) => {
    return axios.post(BASE_URL, { message });
};
