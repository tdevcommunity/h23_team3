import StarRating from '@/components/ui/starRating';
import LanguageIcon from '@/components/ui/languageIcon';
import { Key } from 'react';

const MentorSearchCard = ({ mentor }) => {
    const isBusyStyle = {
        backgroundColor: mentor?.isBusy ? 'lightcoral' : 'lightgreen',
        padding: '5px',
        color: 'black',
        borderRadius: '10px',
        fontSize: '10px',
    };

    return (
        <div className="w-full  max-h-72 shadow-md flex items-center justify-center rounded-lg mb-8 ml-5">
            <div className="flex w-2/3 h-full p-5  flex-col ">
                <div className="flex mb-5">
                    <h1 className="text-purple mr-5">{mentor.stars}</h1>
                    <StarRating rating={mentor.stars} />
                </div>
                <div className="flex mb-5">
                    <LanguageIcon />
                    <div className="flex ml-5">
                        {
                            mentor?.languages?.map((language: String, index: Key) => (
                                <p key={index} style={{
                                    padding: '5px',
                                    color: 'black',
                                    fontSize: '12px'
                                }} >{language}</p>
                            ))
                        }
                    </div>
                </div>
                <div className ="flex flex-wrap">

                    {
                        mentor?.stack?.map((skill, index) => (
                            <p key={index} style={{
                                padding: '5px',
                                color: 'black',
                                fontSize: '12px',
                                border:'solid 1px purple',
                                marginLeft:'3px',
                                borderRadius:'2px'
                            }} >{skill}</p>
                        ))
                    }

                </div>
            </div>
            <div className="  items-center">
                <div className="flex flex-col items-center p-8">
                    <div className="h-24 w-24 rounded-full bg-cover bg-center bg-no-repeat" style={{ backgroundImage: `url(${mentor.image})` }}></div>
                    <p>{mentor.name}</p>
                </div>
                <div>
                    {mentor.isBusy ? (
                        <span className="p-5" style={isBusyStyle}>
                            Indisponible
                        </span>
                    ) : (
                        <span className="p-5" style={isBusyStyle}>
                            Disponible
                        </span>
                    )}
                </div>
            </div>

        </div>
    );
};

export default MentorSearchCard;
