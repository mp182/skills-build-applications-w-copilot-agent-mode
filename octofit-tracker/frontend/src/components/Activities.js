import React, { useEffect, useState } from 'react';

const endpoint = `${process.env.REACT_APP_CODESPACE_NAME ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev` : 'http://localhost:8000'}/api/activities/`;

function Activities() {
  const [activities, setActivities] = useState([]);
  useEffect(() => {
    console.log('Fetching from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setActivities(results);
        console.log('Fetched activities:', results);
      })
      .catch(err => console.error('Error fetching activities:', err));
  }, []);
  return (
    <div>
      <h2>Activities</h2>
      <ul>
        {activities.map((a, i) => (
          <li key={i}>{a.user} - {a.activity} ({a.duration} min)</li>
        ))}
      </ul>
    </div>
  );
}
export default Activities;
