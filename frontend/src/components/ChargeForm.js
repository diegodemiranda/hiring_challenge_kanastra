import React, { useState } from 'react';
import axios from 'axios';

function ChargeForm() {
  const [name, setName] = useState('');
  const [governmentId, setGovernmentId] = useState('');
  const [email, setEmail] = useState('');
  const [debtAmount, setDebtAmount] = useState('');
  const [debtDueDate, setDebtDueDate] = useState('');
  const [status, setStatus] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();

    const charge = {
      name,
      government_id: governmentId,
      email,
      debt_amount: parseFloat(debtAmount),
      debt_due_date: debtDueDate
    };

    try {
      console.log(charge)
      const response = await axios.post(
        `${process.env.REACT_APP_API_URL}/charges`,
        charge,
        {headers: {'Content-Type': 'application/json'}}
      );

      if (response.status === 200) {
        setStatus('Dívida adicionada com sucesso!');
      } else {
        setStatus('Um erro ocorreu durante a solicitação.');
      }

      setName('');
      setGovernmentId('');
      setEmail('');
      setDebtAmount('');
      setDebtDueDate('');
    } catch (error) {
      console.error(error);

      if (error.response) {
        console.error(error.response.status);
        console.error(error.response.headers);
        setStatus('Um erro ocorreu durante a solicitação.');
      } else if (error.request) {
        console.error(error.request);
        setStatus('Um erro ocorreu: Sem resposta do servidor');
      } else {
        console.error('Error', error.message);
        setStatus(`Um erro ocorreu: ${error.message}`);
      }
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Nome:
          <input type="text" name="name" value={name}
                 onChange={e => setName(e.target.value)} required />
        </label>
        <label>
          CPF/CNPJ:
          <input type="text" name="governmentId" value={governmentId}
                 onChange={e => setGovernmentId(e.target.value)} required />
        </label>
        <label>
          Email:
          <input type="email" name="email" value={email}
                 onChange={e => setEmail(e.target.value)} required />
        </label>
        <label>
          Valor da Dívida:
          <input type="number" step="0.01" name="debtAmount" value={debtAmount}
                 onChange={e=> setDebtAmount(e.target.value)} required />
        </label>
        <label>
          Data de Vencimento:
          <input type="text" name="debtDueDate" value={debtDueDate}
                 onChange={e => setDebtDueDate(e.target.value)} required/>
        </label>
        <div className="button-container">
          <button type="submit">CADASTRAR UMA DÍVIDA</button>
        </div>
      </form>
      {status && <p className="status-message">{status}</p>}
    </div>
  );
}

export default ChargeForm;