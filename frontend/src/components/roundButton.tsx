const RoundButton = ({ bgColorClass, content, border }) => {
  const buttonStyle = `${bgColorClass} text-white cursor-pointer rounded-full px-4 py-2  items-center ${border ? 'border border-black' : ''}`;

  return (
    <button className={buttonStyle}>
      {content}
    </button>
  );
}

export default RoundButton;
