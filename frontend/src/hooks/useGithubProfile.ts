
import { useState } from 'react';
import { fetchReport } from '../services/api';

export const useGithubProfile = () => {
    const [report, setReport] = useState<any>(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);

    const getReport = async (username: string) => {
        setLoading(true);
        setError(null);
        try {
            const data = await fetchReport(username);
            setReport(data);
        } catch (e) {
            setError('Error fetching report');
        } finally {
            setLoading(false);
        }
    };

    return { report, loading, error, getReport };
};
