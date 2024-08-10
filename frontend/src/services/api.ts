
import axios from 'axios';

const BASE_URL = 'http://localhost:8000'; // Adjust if necessary

export const fetchReport = async (username: string) => {
    try {
        const response = await axios.get(`${BASE_URL}/report/${username}`);
        return response.data;
    } catch (error) {
        console.error('Error fetching report:', error);
        throw error;
    }
};
