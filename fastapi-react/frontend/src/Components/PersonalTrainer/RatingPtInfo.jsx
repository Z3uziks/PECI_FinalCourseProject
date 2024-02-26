import { GiCardAceSpades } from "react-icons/gi";
import { FaUserCircle } from "react-icons/fa";
import { FaUserGraduate } from "react-icons/fa";
import { FaInfo } from "react-icons/fa";
import { FaStar } from "react-icons/fa";
import { Link,useParams } from "react-router-dom";


const mockedData = [
    {
        name: "Igor Voitenko",
        photo: "https://picsum.photos/250/200",
        decription: "I believe, that through fitness you can change not only your body but your whole life!",
        tags: ["Full Body", "Cardio", "Strength"],
    }
]

export default function RatingPtInfo() {
    const { id } = useParams();
    return (
        <>
           <div role="tablist" className="tabs-bordered mt-6 pb-16 lg:pb-0 w-4/5 lg:w-2/3 mx-auto flex flex-wrap items-center justify-between">
                <Link to={`/PT/${id}/main`} role="tab" className="tab"><FaUserCircle size='15' title='Main'/></Link>
                <Link to={`/PT/${id}/bg`} role="tab" className="tab"><FaUserGraduate size='15' title='Background'/></Link>
                <Link to={`/PT/${id}/other`} role="tab" className="tab"><FaInfo  size='15' title='Info'/></Link>
                <Link to={`/PT/${id}/rating`} role="tab" className="tab-active"><FaStar size='15' title='Rating'/></Link>
            </div>
            <p className="pt-4 text-base font-bold flex items-center justify-center lg:justify-start"><GiCardAceSpades className="h-4 fill-current text-green-700 mr-4" /> What you do</p>
            <p className="pt-2 text-gray-600 text-xs lg:text-sm flex items-center justify-center lg:justify-start"><svg className="h-4 fill-current text-green-700 pr-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M10 20a10 10 0 1 1 0-20 10 10 0 0 1 0 20zm7.75-8a8.01 8.01 0 0 0 0-4h-3.82a28.81 28.81 0 0 1 0 4h3.82zm-.82 2h-3.22a14.44 14.44 0 0 1-.95 3.51A8.03 8.03 0 0 0 16.93 14zm-8.85-2h3.84a24.61 24.61 0 0 0 0-4H8.08a24.61 24.61 0 0 0 0 4zm.25 2c.41 2.4 1.13 4 1.67 4s1.26-1.6 1.67-4H8.33zm-6.08-2h3.82a28.81 28.81 0 0 1 0-4H2.25a8.01 8.01 0 0 0 0 4zm.82 2a8.03 8.03 0 0 0 4.17 3.51c-.42-.96-.74-2.16-.95-3.51H3.07zm13.86-8a8.03 8.03 0 0 0-4.17-3.51c.42.96.74 2.16.95 3.51h3.22zm-8.6 0h3.34c-.41-2.4-1.13-4-1.67-4S8.74 3.6 8.33 6zM3.07 6h3.22c.2-1.35.53-2.55.95-3.51A8.03 8.03 0 0 0 3.07 6z"/></svg> Your Location - 25.0000° N, 71.0000° W</p>
            <p className="pt-8 text-sm">Totally</p>
        </>
        )
}