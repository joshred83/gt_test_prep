import React, { useState } from "react";
import { Line } from "react-chartjs-2";
import { Chart, registerables } from "chart.js";

Chart.register(...registerables);

const functionDict = {
  "sin(x)": Math.sin,
  "cos(x)": Math.cos,
  "x^2": (x) => x * x,
  "e^x": Math.exp,
  "log(x)": (x) => Math.log(Math.max(x, 1e-8)),
};

const methods = [
  "Monte Carlo Integration",
  "Trapezoidal Rule",
  "Simpson's Rule",
];

function App() {
  const [selectedFunction, setSelectedFunction] = useState("sin(x)");
  const [a, setA] = useState(0);
  const [b, setB] = useState(Math.PI);
  const [n, setN] = useState(32);
  const [selectedMethods, setSelectedMethods] = useState(["Monte Carlo Integration"]);
  const [results, setResults] = useState([]);
  const [chartData, setChartData] = useState(null);

  const integrate = () => {
    const f = functionDict[selectedFunction];
    const exactValue = numericIntegration(f, a, b);
    let newResults = [];
    let dataPoints = [];

    selectedMethods.forEach((method) => {
      let estimate;
      if (method === "Monte Carlo Integration") estimate = monteCarlo(f, a, b, n);
      else if (method === "Trapezoidal Rule") estimate = trapezoidal(f, a, b, n);
      else if (method === "Simpson's Rule") estimate = simpsons(f, a, b, n);

      newResults.push({ method, estimate, error: Math.abs(estimate - exactValue) });
    });

    for (let x = a; x <= b; x += (b - a) / 100) {
      dataPoints.push({ x, y: f(x) });
    }

    setResults(newResults);
    setChartData({
      labels: dataPoints.map((p) => p.x.toFixed(2)),
      datasets: [
        {
          label: selectedFunction,
          data: dataPoints.map((p) => p.y),
          borderColor: "blue",
          fill: false,
        },
      ],
    });
  };

  const monteCarlo = (f, a, b, n) => {
    let sum = 0;
    for (let i = 0; i < n; i++) {
      let x = Math.random() * (b - a) + a;
      sum += f(x);
    }
    return ((b - a) / n) * sum;
  };

  const trapezoidal = (f, a, b, n) => {
    let h = (b - a) / n;
    let sum = (f(a) + f(b)) / 2;
    for (let i = 1; i < n; i++) {
      sum += f(a + i * h);
    }
    return h * sum;
  };

  const simpsons = (f, a, b, n) => {
    if (n % 2 !== 0) n++; // Simpson's rule requires an even n
    let h = (b - a) / n;
    let sum = f(a) + f(b);
    for (let i = 1; i < n; i++) {
      sum += f(a + i * h) * (i % 2 === 0 ? 2 : 4);
    }
    return (h / 3) * sum;
  };

  const numericIntegration = (f, a, b) => {
    let step = (b - a) / 1000;
    let sum = 0;
    for (let x = a; x < b; x += step) {
      sum += f(x) * step;
    }
    return sum;
  };

  return (
    <div>
      <h1>Numerical Integration Visualization</h1>
      <label>
        Function:
        <select value={selectedFunction} onChange={(e) => setSelectedFunction(e.target.value)}>
          {Object.keys(functionDict).map((fn) => (
            <option key={fn} value={fn}>{fn}</option>
          ))}
        </select>
      </label>
      <br />
      <label>
        Lower Limit (a):
        <input type="number" value={a} onChange={(e) => setA(Number(e.target.value))} />
      </label>
      <br />
      <label>
        Upper Limit (b):
        <input type="number" value={b} onChange={(e) => setB(Number(e.target.value))} />
      </label>
      <br />
      <label>
        Number of intervals (n):
        <input type="number" value={n} onChange={(e) => setN(Number(e.target.value))} />
      </label>
      <br />
      <label>
        Integration Methods:
        <br />
        {methods.map((method) => (
          <label key={method}>
            <input
              type="checkbox"
              checked={selectedMethods.includes(method)}
              onChange={() =>
                setSelectedMethods((prev) =>
                  prev.includes(method)
                    ? prev.filter((m) => m !== method)
                    : [...prev, method]
                )
              }
            />
            {method}
          </label>
        ))}
      </label>
      <br />
      <button onClick={integrate}>Calculate</button>
      <h2>Results</h2>
      <ul>
        {results.map((res) => (
          <li key={res.method}>
            {res.method}: Estimate = {res.estimate.toFixed(6)}, Error = {res.error.toFixed(6)}
          </li>
        ))}
      </ul>
      {chartData && <Line data={chartData} />} 
    </div>
  );
}

export default App;
