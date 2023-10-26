import FilterBar from '@/components/ui/mentor/filterBar'
import Navbar from '@/components/ui/navbar';
import BlockFooter from '../_blocks/blockFooter';

export default function Mentors ()  {
    return (
        <section className='bg-gray-100 '>
            <FilterBar />
            <BlockFooter/>
        </section>
    )
}

