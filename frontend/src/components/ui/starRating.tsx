import React from 'react';
import StarIcon from '@/components/ui/starIcon';
import HalfStar from '@/components/ui/halfStar';

const StarRating = ({ rating }) => {
  // Calculate the number of full stars and the remainder for the half star.
  const fullStars = Math.floor(rating);
  const hasHalfStar = rating % 1 !== 0;

  // Create an array of JSX elements to represent the stars and half star.
  const stars = [];
  for (let i = 0; i < fullStars; i++) {
    stars.push(<StarIcon key={i} />);
  }
  if (hasHalfStar) {
    stars.push(<HalfStar key={fullStars} />);
  }

  return (
    <div style={{display:'flex'}}>
      {stars.map((star, index) => (
        <span key={index}  style={{color:'purple'}} >{star}</span>
      ))}
    </div>
  );
};

export default StarRating;
