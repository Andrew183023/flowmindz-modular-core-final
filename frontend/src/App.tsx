import React from 'react';

export default function App() {
  return (
    <div className="flex flex-col items-center justify-center h-screen gap-6">
      <h1 className="text-4xl font-bold text-purple-400 animate-pulse">🚀 FlowMindz Panel</h1>
      <p className="text-lg text-gray-300">Sistema operacional inteligente ativado.</p>
      <div className="border border-purple-500 rounded-lg p-6 bg-gray-800 shadow-lg">
        <p className="text-green-400 font-semibold">✅ IA Ativa</p>
        <p className="text-blue-400 font-semibold">✅ Banco Conectado</p>
        <p className="text-yellow-400 font-semibold">✅ Painel Web Online</p>
      </div>
    </div>
  );
}
