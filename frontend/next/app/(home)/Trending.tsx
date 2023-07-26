import Link from 'node_modules/next/link';
import React from 'react'
import Image from "next/image";
import Pagination from '../(shared)/Pagination';

type TrendingCardProps = {
    className?: string;
    image: string;
};

const TrendingCard = ({ className, image }: TrendingCardProps) => {
    return (
        <Link className={`${className} sm:mt-0 sm:h-auto relative mt-7 block w-full h-96 hover:opacity-70`} href='/'>
            <div className="z-0 relative w-full h-full">
                <Image
                fill
                alt="trend"
                src={`/assets/${image}`}
                sizes="(max-width: 480px) 100vw,
                        (max-width: 768px) 75vw,
                        (max-width: 1060px) 50vw,
                        33vw"
                style={{ objectFit: "cover" }}
                />
            </div>
            <div className={"absolute z-1 top-0 left-0 w-full h-full bg-gradiest-gradual"}/>
            <div className={"absolute z-2 left-0 p-3 bottom-0"}>
                <h4 className="inline-block px-5 py-1 font-semibold bg-accent-orange text-wh-50">


                </h4>
                <div className="text-wh-100 mt-2">
                    Post Title
                </div>
            </div>

        </Link>
    )
}

type Props = {};

const Trending = (props: Props) => {
    return (        
        <section className="pt-3 pb-10">
            <div className = "flex items-center gap-3">
                <div className="bg-wh-900 py-2 px-8 text-wh-10 text-sm font-bold">
                    LATEST
                </div>
                <p className="text-sm">
                    Nunc enim lobortis quam risus et feugiat nibh eu ornare. Molestie sit
                    nulla dolor diam turpis.
                </p>
            </div>
            <div className="sm:grid gap-5 grid-cols-4 grid-rows-2 sm:h-[600px]">
                <TrendingCard image="NoMash_22_NoShirtNoShoes_FB-01.png" className="col-span-2 row-span-2 bg-wh-500"/>
            <TrendingCard image={"download.jpeg"} className="col-span-2 row-span-1 bg-wh-500"/>
            <TrendingCard image={"download.jpeg"} className="col-span-1 row-span-1 bg-wh-500"/>
            <TrendingCard image={"download.jpeg"} className="col-span-1 row-span-1 bg-wh-500"/>
            </div>
            <Pagination />
        </section>
    )

    
} 

export default Trending
