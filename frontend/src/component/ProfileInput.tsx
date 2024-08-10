import React, { useState } from 'react';

interface ProfileInputProps {
    onSubmit: (username: string) => void;
}

const ProfileInput: React.FC<ProfileInputProps> = ({ onSubmit }) => {
    const [username, setUsername] = useState('');

    const handleSubmit = (event: React.FormEvent) => {
        event.preventDefault();
        onSubmit(username);
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                GitHub Username:
                <input
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required
                />
            </label>
            <button type="submit">Get Report</button>
        </form>
    );
};

export default ProfileInput;
