// script.js

// Sample data
const teams = [
    { team: "Team A", wins: 10, losses: 2, points: 30 },
    { team: "Team B", wins: 8, losses: 4, points: 24 },
    { team: "Team C", wins: 7, losses: 5, points: 21 },
    { team: "Team D", wins: 5, losses: 7, points: 15 },
    { team: "Team E", wins: 3, losses: 9, points: 9 },
];

// Function to sort teams by points, wins, and losses
function sortTeams(teams) {
    return teams.sort((a, b) => b.points - a.points || b.wins - a.wins || a.losses - b.losses);
}

// Function to generate standings table
function generateStandings() {
    const sortedTeams = sortTeams(teams);
    const tableBody = document.querySelector('#standings tbody');

    sortedTeams.forEach((team, index) => {
        const row = document.createElement('tr');

        row.innerHTML = `
            <td>${index + 1}</td>
            <td>${team.team}</td>
            <td>${team.wins}</td>
            <td>${team.losses}</td>
            <td>${team.points}</td>
        `;

        tableBody.appendChild(row);
    });
}

// Generate the standings when the page loads
document.addEventListener('DOMContentLoaded', generateStandings);
