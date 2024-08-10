import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { fetchReport } from '../services/api';

const Report: React.FC = () => {
    const { username } = useParams<{ username: string }>();
    const [report, setReport] = useState<any>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const getReport = async () => {
            if (!username) {
                setError('Username is required');
                setLoading(false);
                return;
            }

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

        getReport();
    }, [username]);

    return (
        <div>
            <h1>GitHub Profile Report for {username}</h1>
            {loading && <p>Loading...</p>}
            {error && <p>{error}</p>}
            {report && (
                <div>
                    <h2>Report Details</h2>
                    <div>
                        <img src={report.avatar_url} alt={report.username} />
                        <h3>{report.name}</h3>
                        <p>{report.bio}</p>
                    </div>
                    <div>
                        <h4>Advanced Analysis</h4>
                        <p>{report.advanced_analysis}</p>
                    </div>
                    <div>
                        <h4>Tech Stack</h4>
                        <ul>
                            {report.tech_stack.map((tech: any) => (
                                <li key={tech.language}>{tech.language}: {tech.count}</li>
                            ))}
                        </ul>
                    </div>
                    <div>
                        <h4>Experience</h4>
                        <p>Total Repositories: {report.experience.total_repos}</p>
                        <p>Total Stars: {report.experience.total_stars}</p>
                        <p>Total Forks: {report.experience.total_forks}</p>
                        <p>Total Watchers: {report.experience.total_watchers}</p>
                    </div>
                    <div>
                        <h4>Impact Score</h4>
                        <p>{report.impact_score}</p>
                    </div>
                    {report.pdf_url && (
                        <div>
                            <h4>Download Report</h4>
                            <a href={report.pdf_url} download>
                                Download PDF
                            </a>
                        </div>
                    )}
                </div>
            )}
        </div>
    );
};

export default Report;
