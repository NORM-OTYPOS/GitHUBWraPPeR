import React from 'react';

interface ReportCardProps {
    report: any;
}

const ReportCard: React.FC<ReportCardProps> = ({ report }) => {
    return (
        <div>
            <h2>GitHub User Report</h2>
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
        </div>
    );
};

export default ReportCard;
