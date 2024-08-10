import React from 'react';
import ProfileInput from './ProfileInput';
import ReportCard from './ReportCard';
import { useGithubProfile } from '../hooks/useGithubProfile';

const Dashboard: React.FC = () => {
    const { report, loading, error, getReport } = useGithubProfile();

    return (
        <div>
            <h1>GitHub Profile Report Generator</h1>
            <ProfileInput onSubmit={getReport} />
            {loading && <p>Loading...</p>}
            {error && <p>{error}</p>}
            {report && <ReportCard report={report} />}
        </div>
    );
};

export default Dashboard;
