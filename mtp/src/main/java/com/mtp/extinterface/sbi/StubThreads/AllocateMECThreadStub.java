/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mtp.extinterface.sbi.StubThreads;

import com.mtp.SingletonEventBus;
import com.mtp.common.objects.DomainElem;
import com.mtp.events.resourcemanagement.ComputeAllocation.ComputeAllocateMECReply;
import com.mtp.events.resourcemanagement.ComputeAllocation.ComputeAllocateMECReq;

/**
 *
 * @author efabuba
 */
public class AllocateMECThreadStub extends Thread {
    private DomainElem dominfo;
    private ComputeAllocateMECReq request;

 
    public AllocateMECThreadStub (DomainElem val, ComputeAllocateMECReq req) {
        dominfo = val;
        request = req;
    }
    
    @Override
    public void run() {
        //TODO: perform action to MEC list for MEC domain
        
        
        ComputeAllocateMECReply ev = new ComputeAllocateMECReply(request.getReqid(), request.getServid(),
                        request.getMecdomid(), "10", request.getVmreq());
        //TODO: prepare event to collect info
        //send event
        SingletonEventBus.getBus().post(ev);
    }   
}
