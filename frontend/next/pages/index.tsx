import React from "react";
import Shop from "app/(home)/Shop";
import Tracks from "app/(home)/Tracks";
import Trending from "app/(home)/Trending";
import Layout from '../app/layout';
import type { Metadata, GetServerSideProps } from 'next'

import { DefaultApi } from 'generated-typescript-client/apis/DefaultApi';
import { Configuration } from 'generated-typescript-client/runtime';

const api = new DefaultApi(new Configuration({ basePath: 'http://localhost:8080' }));


interface Props {
    data: any;
}

export const metadata: Metadata = {
    title: 'NoMashSound',
    description: 'No Mash Sound e-commerce site',
}
  

export default function Home({ data }: Props) {
    return (
        <Layout >
            <div className="px-10 leading-7">
                <Trending />
                <div className="md:flex gap-10 mb-5">
                    <div className="basis-full">
                        <Tracks data={data}></Tracks>
                        <Shop images={[]} ></Shop>
                    </div>
                </div>
            </div>
        </Layout> 
    ) 
}

export const getServerSideProps: GetServerSideProps<Props> = async () => {
    try {
      console.log('Fetching data...');
      const res = await api.homeGet();
      const data = res.body !== undefined ? res.body : null;
      return { props: { data } };
    } catch (error) {
      console.error('Error fetching data:', error);
      return { props: { data: null } }; // Return a default value or handle the error case appropriately
    }
  };